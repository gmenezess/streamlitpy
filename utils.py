import pandas as pd
import numpy as np

def generate_option(S, K, tipo, acao, premio = 0):
    """
    Calcula o payoff de uma opção de compra (call option) ou opção de venda (put option),
    dependendo se a opção é comprada ou vendida.

    Parâmetros:
        S (array): Preço do ativo subjacente.
        K (float): Preço de exercício da opção.
        tipo (str): Tipo de opção ('call' para opção de compra, 'put' para opção de venda).
        acao (str): Ação realizada ('compra' para comprar a opção, 'venda' para vender a opção).

    Retorna:
        array: Payoff da opção correspondente para cada preço do ativo subjacente.
    """
    if tipo == 'call':
        if acao == 'compra':
            return np.maximum(S - K, 0) - premio
        elif acao == 'venda':
            return np.maximum(S - K, 0) * -1 + premio
    elif tipo == 'put':
        if acao == 'compra':
            return np.maximum(K - S, 0) - premio
        elif acao == 'venda':
            return np.maximum(K - S, 0) * -1 + premio
    else:
        raise ValueError("Tipo de opção inválido. Use 'call' para opção de compra ou 'put' para opção de venda.")
