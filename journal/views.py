from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from .permissions import IsOwner

class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated, IsOwner]
# ...resto da classe
class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas as entradas do usuário autenticado
        return JournalEntry.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        # Define o autor automaticamente ao criar a entrada
        serializer.save(author=self.request.user)
    