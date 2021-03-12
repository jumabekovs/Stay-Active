from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import OfferForm
from .models import Card, Offer
from ..user.models import User


class CardsView(ListView):
    model = Card
    template_name = 'applications/cards.html'
    context_object_name = 'cards'




def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(User, Offer, fields=('card', 'status'))
    customer = User.objects.get(id=pk)
    # form = OrderForm(initial={'customer': customer})   #this will fill automatically the user
    formset = OrderFormSet(queryset=Offer.objects.none(), instance=customer)     # We used it when creating order form
    if request.method == "POST":
        # print('Printing POST:', request.POST) to check what we are sending
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer) # just added request.POST
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}  #changed from form to formset
    return render(request, 'accounts/order_form.html', context)



def updateOrder(request, pk):
    order = Offer.objects.get(id=pk)
    form = OfferForm(instance=order)

    if request.method == "POST":
        form = OfferForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)



def deleteOrder(request, pk):
    order = Offer.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)