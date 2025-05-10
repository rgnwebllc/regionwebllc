from accounts.models import Subscription

def subscription_status(request):
    if request.user.is_authenticated:
        subscription = Subscription.objects.filter(user=request.user).first()
        return {'subscription': subscription}
    return {}