from django.shortcuts import render
from ticket.models import TicketModel


def ticket(request):
    return render(request, 'ticket/ticket.html')


def recent_tickets(request):
    all_tickets = TicketModel.objects.all().order_by('-created_at')
    return render(request, 'ticket/ticket.html', {'all_tickets': all_tickets})


# def ticket_by_id(request, ticket_id):
#     ticket = TicketModel.objects.get(pk=ticket_id)
#     return render(request, 'ticket/ticket.html', {'ticket': ticket})


def test(request):
    return render(request, 'ticket/test.html')


def experiment(request):
    return render(request, 'ticket/experiment.html')
