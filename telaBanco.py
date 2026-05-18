from conta import Conta
contaGuilherme = Conta("Guilherme", "123.456.789-00", 500, "1234", 5678)
contaGuilherme.extrato()

# CRIAR OS SEGUINTES MÉTODOS:
contaGuilherme.sacar(1000)
contaGuilherme.extrato(250)

conta2 = Conta("Fulaino", "123.456.789-00", 500, "9999", 1234)
contaGuilherme.pix(conta2, 250)