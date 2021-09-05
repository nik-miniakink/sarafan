import arrow

from django.db.models import Avg, Max, Sum
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.fitness.models import Activity
from app.fitness.serializer import ActivitySerializer


class ActivityCreate(generics.CreateAPIView):
    """
    Создает запись активности
    """
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def agregate_statictic(request, gap):
    """
    Выгружает статистические данные по запросу пользователя за последние gap часов
    """
    past_time = arrow.now().shift(hours=-gap).datetime
    now = arrow.now().datetime
    print(now)
    print(past_time)
    queryset = Activity.objects.filter(user=request.user, start_time__gte=past_time)
    counter = queryset.count()

    info = queryset.aggregate(
        Avg('distance'), Avg('calories'),
        Max('distance'), Max('calories'),
        Sum('distance'), Sum('calories')
    )

    info_by_type = list(queryset.values('type').annotate(Sum('distance'), Sum('calories')))

    return JsonResponse({
        'time': gap,
        'counter': counter,
        'info': info,
        'info_by_type': info_by_type,
    }
    )
