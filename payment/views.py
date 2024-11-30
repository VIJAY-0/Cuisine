import razorpay
from django.conf import settings
from django.http import JsonResponse

client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))

def initiate_payment(request):
    amount = 50000  # In paisa (e.g., 500.00 INR)
    order = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return JsonResponse(order)

def verify_payment(request):
    data = request.POST
    client.utility.verify_payment_signature(data)  # Verify signature
    return JsonResponse({'status': 'success'})
