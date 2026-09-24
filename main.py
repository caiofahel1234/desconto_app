from src.models.desconto import DescontoVIP, DescontoNormal, DescontoPremium
from src.models.pedido import Pedido
from src.repositories.pedido_repository import PedidoRepository
from src.controllers.pedido_controller import PedidoController
from src.services.pedido_service import PedidoService


if __name__ == "__main__":
    repo = PedidoRepository()
    service = PedidoService(repo)
    controller = PedidoController(service)

   pedido1 = Pedido("")