import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment_success(request):
    return render(request, 'payments/success.html')


def payment_cancel(request):
    return render(request, 'payments/cancel.html')

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        
        product_id = data.get('product_id')
        if not product_id:
            return JsonResponse({'error': 'Product ID missing'}, status=400)

        try:
            product = Product.objects.get(id=product_id)

            YOUR_DOMAIN = 'http://127.0.0.1:8000'  # or your live domain
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {'name': product.name},
                        'unit_amount': int(product.price * 100),  # Convert dollars to cents
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=YOUR_DOMAIN + '/payments/success/',
                cancel_url=YOUR_DOMAIN + '/payments/cancel/',
            )
            return JsonResponse({'id': session.id})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return HttpResponseBadRequest('Invalid request method')