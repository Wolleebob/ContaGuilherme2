from conta import Conta
conta1 = Conta("Guilherme", "432.567.876-99", 800, "4567", 8990)
conta1.extrato()
conta1.depositar(500)
conta1.sacar(300)
conta1.titular = "Guilherme2"
conta1.extrato()
conta2 = Conta("Fulaino", "123.456.789-00", 500, "9999", 1234)
conta1.transferir(400, conta2)
conta2.extrato()
conta1.extrato()