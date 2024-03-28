import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from utils import *

df_options = pd.DataFrame()

def main():
    st.set_page_config(
        layout="wide",
        page_title="Options Dashboard"
    )


    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Secas", "Straddle","Strangle", "Collar", "Criar"])

    with tab1:
        st.header("Opções secas")
        
        def_secas = st.checkbox('O que é?')
        if def_secas:
            st.markdown("""
                        Operar opções a seco nada mais é do que comprar ou vender uma call ou uma put na expectativa de lucrar com a alta ou com a queda do ativo-objeto. Ela é uma estratégia muito procurada por quem está começando a se familiarizar com as opções porque tem baixo custo, é fácil de entender e não requer a compra de ações para ser executada.
                        """)
        
        def_calculo = st.checkbox('Calculo')
        if def_calculo:
            st.markdown("aa")
        
        def_mais = st.checkbox('Mais...')
        if def_mais:
            st.subheader("Opções Dentro do Dinheiro (ITM)")
            st.markdown("Uma opção dentro do dinheiro (in the money; ITM), é uma opção de compra cujo ativo objeto está sendo negociado no mercado à vista a um preço superior ao preço de exercício da opção, ou seja, se fosse o momento do vencimento, seu detentor certamente a exerceria. Pelo contrário, uma opção de venda estará dentro do dinheiro quando o preço do ativo no mercado à vista estiver abaixo do preço de exercício da opção.")
            st.subheader("Opções Fora do Dinheiro (OTM)")
            st.markdown("Uma opção fora do dinheiro (out of the money; OTM) é aquela em que o exercício não compensaria se estivesse no momento de seu vencimento. É uma opção de compra com o preço de seu ativo objeto abaixo do preço de exercício do contrato, ou da mesma forma, uma opção de venda com o preço do ativo acima do seu preço de exercício.")
            st.subheader("Opções No Dinheiro (ATM)")
            st.markdown("Uma opção “no dinheiro” (ou “at the money”; ATM) é aquela em que o preço do ativo subjacente é igual ao preço de exercício. Ela pode ser uma opção de venda ou de compra. Isso torna difícil prever se essa opção será exercida ou não. No entanto, como a probabilidade de um preço de exercício específico ocorrer no mercado é pequena, consideram-se “no dinheiro” as opções que estejam suficientemente próximas do preço de exercício.")
        
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            strike = st.number_input('Strike', value=100)

        with col2:
            premio = st.number_input('Premio', value = 30)

        with col3:
            values = st.slider(
                'Intervalo do Ativo Objeto',
                0, 500, (0, 200))
            
            S = np.linspace(values[0],values[1], values[1]-values[0]+1)

        col_call, col_put = st.columns(2)
        with col_call:
            st.markdown(f'<h3 style="text-align: center;">Payoff Call strike {strike}</h3>', unsafe_allow_html=True)

            with st.container(border=True):
                payoff_call_compra = generate_option(S, strike, 'call', 'compra', premio)
                payoff_call_venda = generate_option(S, strike, 'call', 'venda', premio)

                fig_call = go.Figure()

                # Adicionando linhas ao gráfico
                fig_call.add_trace(go.Scatter(x=S, y=payoff_call_compra, mode='lines', name='Pos. Comprada', line=dict(color='green')))
                fig_call.add_trace(go.Scatter(x=S, y=payoff_call_venda, mode='lines', name='Pos. Vendida', line=dict(color='red')))
                fig_call.add_vline(x=strike, line_dash='dash', line_color='blue', line_width=1)

                fig_call.add_annotation(
                    x=strike,
                    y=0,  # Posição y da anotação
                    text='K',
                    showarrow=True,
                    arrowhead=1,
                    font=dict(
                        family='Arial',
                        size=12,
                        color='blue'
                    ),
                )

                # Configurando layout do gráfico
                fig_call.update_layout(
                    xaxis_title='Ativo Objeto no Vencimento',
                    yaxis_title='PnL',
                    legend=dict(
                        orientation='h',  # horizontal
                        y=1.1,  # posicionar a legenda acima do gráfico
                        x=0.5,  # centralizar a legenda
                        xanchor='center',
                        bgcolor='rgba(255, 255, 255, 0)',  # tornar o fundo da legenda transparente
                        bordercolor='rgba(255, 255, 255, 0)'  # tornar a borda da legenda transparente
                    ),
                    autosize=True,
                )

                st.plotly_chart(fig_call, use_container_width=True)

        with col_put:
            st.markdown(f'<h3 style="text-align: center;">Payoff Put (strike {strike})</h3>', unsafe_allow_html=True)
            
            with st.container(border=True):
                payoff_put_compra = generate_option(S, strike, 'put', 'compra', premio)
                payoff_put_venda = generate_option(S, strike, 'put', 'venda', premio)

                fig_put = go.Figure()

                # Adicionando linhas ao gráfico
                fig_put.add_trace(go.Scatter(x=S, y=payoff_put_compra, mode='lines', name='Pos. Comprada', line=dict(color='green')))
                fig_put.add_trace(go.Scatter(x=S, y=payoff_put_venda, mode='lines', name='Pos. Vendida', line=dict(color='red')))
                fig_put.add_vline(x=strike, line_dash='dash', line_color='blue', line_width=1)

                fig_put.add_annotation(
                    x=strike,
                    y=0,  # Posição y da anotação
                    text='K',
                    showarrow=True,
                    arrowhead=1,
                    font=dict(
                        family='Arial',
                        size=12,
                        color='blue'
                    ),
                )

                # Configurando layout do gráfico
                fig_put.update_layout(
                    xaxis_title='Ativo Objeto no Vencimento',
                    yaxis_title='PnL',
                    legend=dict(
                        orientation='h',  # horizontal
                        y=1.1,  # posicionar a legenda acima do gráfico
                        x=0.5,  # centralizar a legenda
                        xanchor='center',
                        bgcolor='rgba(255, 255, 255, 0)',  # tornar o fundo da legenda transparente
                        bordercolor='rgba(255, 255, 255, 0)'  # tornar a borda da legenda transparente
                    ),
                    autosize=True,
                )

                # Exibindo o gráfico no Streamlit
                st.plotly_chart(fig_put, use_container_width=True)
    
    # --Straddle
    with tab2:
        st.header("Straddle")

        def_straddle = st.checkbox('O que é?', key=1)
        if def_straddle:
            st.markdown("""
                        A estratégia de straddle é quando o investidor compra duas opções, uma call e uma put, com o mesmo preço de exercício (strike) e o mesmo vencimento. Essa estratégia é utilizada quando se espera uma grande mudança no preço do ativo, mas não se sabe em qual direção.
                        """)
            
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            strike_straddle = st.number_input('Strike', value=100, key=2)

        with col2:
            premio_straddle = st.number_input('Premio', value = 30, key=3)

        with col3:
            values = st.slider(
                'Intervalo do Ativo Objeto',
                0, 500, (0, 200), key=4)
            
            S = np.linspace(values[0],values[1], values[1]-values[0]+1)

        st.markdown(f'<h3 style="text-align: center;">Payoff Straddle (strike {strike_straddle})</h3>', unsafe_allow_html=True)

        with st.container(border=True):

            payoff_call = generate_option(S, strike_straddle, 'call', 'compra')
            payoff_put = generate_option(S, strike_straddle, 'put', 'compra')
            payoff_estrutura = payoff_call+payoff_put-premio_straddle

            fig_straddle = go.Figure()

            # Adicionando linhas ao gráfico
            fig_straddle.add_trace(go.Scatter(x=S, y=payoff_estrutura, mode='lines', name='Pos. Comprada', line=dict(color='green')))
            show_options = st.checkbox("Mostrar composição")
            if show_options:
                fig_straddle.add_trace(go.Scatter(x=S, y=payoff_call, mode='lines', name='Call', line=dict(color='darkgrey', dash='dash')))
                fig_straddle.add_trace(go.Scatter(x=S, y=payoff_put, mode='lines', name='Put', line=dict(color='lightgrey', dash='dash')))
                
            fig_straddle.add_vline(x=strike, line_dash='dash', line_color='blue', line_width=1)

            fig_straddle.add_annotation(
                x=strike,
                y=0,  # Posição y da anotação
                text='K',
                showarrow=True,
                arrowhead=1,
                font=dict(
                    family='Arial',
                    size=12,
                    color='blue'
                ),
            )

            # Configurando layout do gráfico
            fig_straddle.update_layout(
                xaxis_title='Ativo Objeto no Vencimento',
                yaxis_title='PnL',
                legend=dict(
                    orientation='h',  # horizontal
                    y=1.1,  # posicionar a legenda acima do gráfico
                    x=0.5,  # centralizar a legenda
                    xanchor='center',
                    bgcolor='rgba(255, 255, 255, 0)',  # tornar o fundo da legenda transparente
                    bordercolor='rgba(255, 255, 255, 0)'  # tornar a borda da legenda transparente
                ),
                autosize=True,
            )

            # Exibindo o gráfico no Streamlit
            st.plotly_chart(fig_straddle, use_container_width=True)

    # --Strangle
    with tab3:
        st.header("Strangle")

        def_strangle = st.checkbox('O que é?', key=5)
        if def_strangle:
            st.markdown("""
                        A estratégia de strangle é muito parecida com a do straddle, mas envolve a compra de opções de compra e venda com preços de exercício diferentes, com o objetivo de reduzir o custo da estratégia.
                        """)
            
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            strike_call = st.number_input('Strike da Call', value=90, key=6)

        with col2:
            strike_put = st.number_input('Strike da Put', value=110, key=7)

        with col3:
            premio = st.number_input('Premio', value = 30, key=8)

        with col4:
            values = st.slider(
                'Intervalo do Ativo Objeto',
                0, 500, (0, 200), key=9)
            
            S = np.linspace(values[0],values[1], values[1]-values[0]+1)

        st.markdown(f'<h3 style="text-align: center;">Payoff Strangle (strike Call {strike_call} e strike Put {strike_put})</h3>', unsafe_allow_html=True)

        with st.container(border=True):

            payoff_call = generate_option(S, strike_call, 'call', 'compra')
            payoff_put = generate_option(S, strike_put, 'put', 'compra')
            payoff_estrutura = payoff_call+payoff_put-premio

            fig_strangle = go.Figure()

            # Adicionando linhas ao gráfico
            fig_strangle.add_trace(go.Scatter(x=S, y=payoff_estrutura, mode='lines', name='Strangle', line=dict(color='green')))
            show_options = st.checkbox("Mostrar composição", key=10)
            if show_options:
                fig_strangle.add_trace(go.Scatter(x=S, y=payoff_call, mode='lines', name='Call', line=dict(color='darkgrey', dash='dash')))
                fig_strangle.add_trace(go.Scatter(x=S, y=payoff_put, mode='lines', name='Put', line=dict(color='lightgrey', dash='dash')))
                
            fig_strangle.add_vline(x=strike_call, line_dash='dash', line_color='blue', line_width=1)
            fig_strangle.add_vline(x=strike_put, line_dash='dash', line_color='blue', line_width=1)

            fig_strangle.add_annotation(
                x=strike_call,
                y=0,  # Posição y da anotação
                text='Kcall',
                showarrow=True,
                arrowhead=1,
                font=dict(
                    family='Arial',
                    size=12,
                    color='blue'
                ),
            )

            fig_strangle.add_annotation(
                x=strike_put,
                y=0,  # Posição y da anotação
                text='Kput',
                showarrow=True,
                arrowhead=1,
                font=dict(
                    family='Arial',
                    size=12,
                    color='blue'
                ),
            )

            # Configurando layout do gráfico
            fig_strangle.update_layout(
                xaxis_title='Ativo Objeto no Vencimento',
                yaxis_title='PnL',
                legend=dict(
                    orientation='h',  # horizontal
                    y=1.1,  # posicionar a legenda acima do gráfico
                    x=0.5,  # centralizar a legenda
                    xanchor='center',
                    bgcolor='rgba(255, 255, 255, 0)',  # tornar o fundo da legenda transparente
                    bordercolor='rgba(255, 255, 255, 0)'  # tornar a borda da legenda transparente
                ),
                autosize=True,
            )

            # Exibindo o gráfico no Streamlit
            st.plotly_chart(fig_strangle, use_container_width=True)


    # --Collar
    with tab4:
        st.header("Collar")

        def_strangle = st.checkbox('O que é?', key=11)
        if def_strangle:
            st.markdown("""
                        Um "collar" é uma estrutura que é composta pela compra do papel, venda de uma Call fora do dinheiro (OTM) e a compra de uma Put OTM, com a opção de compra e a opção de venda tendo o mesmo vencimento. A compra da Put no "collar" atua como proteção para as ações compradas (potencialmente limitando suas perdas), e a venda da Call ajuda a financiar a compra da Put.
                        """)
            
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            strike_call = st.number_input('Strike da Call', value=120.00, format="%.2f", key=12)
            premio_call = st.number_input('Premio da Call', value = 20.00, format="%.2f", key=17)

        with col2:
            strike_put = st.number_input('Strike da Put', value=80.00, format="%.2f", key=13)
            premio_put = st.number_input('Premio da Put', value = 10.00, format="%.2f", key=18)

        with col3:
            values = st.slider(
                'Intervalo do Ativo Objeto',
                0, 500, (0, 200), key=15)
            
            S = np.linspace(values[0],values[1], values[1]-values[0]+1)

        st.markdown(f'<h3 style="text-align: center;">Payoff Strangle (strike Call {strike_call} e strike Put {strike_put})</h3>', unsafe_allow_html=True)

        payoff_call = generate_option(S, strike_call, 'call', 'venda', premio_call)
        payoff_put = generate_option(S, strike_put, 'put', 'compra', premio_put)
        payoff_papel = S
        payoff_estrutura = S + payoff_call + payoff_put
        custo_estrutura = premio_call-premio_put

        with col4:
            st.markdown("Financeiro da estrutura:")
            if custo_estrutura >= 0:
                st.markdown(f"+ R${custo_estrutura}")
            else:
                st.markdown(f"- R${custo_estrutura}")

        with st.container(border=True):
            
            fig_colar = go.Figure()

            # Adicionando linhas ao gráfico
            fig_colar.add_trace(go.Scatter(x=S, y=payoff_estrutura, mode='lines', name='Strangle', line=dict(color='green')))
            show_options = st.checkbox("Mostrar composição", key=16)
            if show_options:
                fig_colar.add_trace(go.Scatter(x=S, y=payoff_call, mode='lines', name='Call', line=dict(color='darkgrey', dash='dash')))
                fig_colar.add_trace(go.Scatter(x=S, y=payoff_put, mode='lines', name='Put', line=dict(color='lightgrey', dash='dash')))
                fig_colar.add_trace(go.Scatter(x=S, y=S, mode='lines', name='Papel', line=dict(color='grey', dash='dash')))

            fig_colar.add_vline(x=strike_call, line_dash='dash', line_color='blue', line_width=1)
            fig_colar.add_vline(x=strike_put, line_dash='dash', line_color='blue', line_width=1)

            fig_colar.add_annotation(
                x=strike_call,
                y=0,  # Posição y da anotação
                text='Kcall',
                showarrow=True,
                arrowhead=1,
                font=dict(
                    family='Arial',
                    size=12,
                    color='blue'
                ),
            )

            fig_colar.add_annotation(
                x=strike_put,
                y=0,  # Posição y da anotação
                text='Kput',
                showarrow=True,
                arrowhead=1,
                font=dict(
                    family='Arial',
                    size=12,
                    color='blue'
                ),
            )

            # Configurando layout do gráfico
            fig_colar.update_layout(
                xaxis_title='Ativo Objeto no Vencimento',
                yaxis_title='PnL',
                legend=dict(
                    orientation='h',  # horizontal
                    y=1.1,  # posicionar a legenda acima do gráfico
                    x=0.5,  # centralizar a legenda
                    xanchor='center',
                    bgcolor='rgba(255, 255, 255, 0)',  # tornar o fundo da legenda transparente
                    bordercolor='rgba(255, 255, 255, 0)'  # tornar a borda da legenda transparente
                ),
                autosize=True,
            )

            # Exibindo o gráfico no Streamlit
            st.plotly_chart(fig_colar, use_container_width=True)

    with tab5:
        st.header("Crie sua estrutura")
        col1, col2 = st.columns(2)

        if 'df_options' not in st.session_state:
            st.session_state.df_options = pd.DataFrame()

        with col1:
            def adicionar_linha(df, input_tipo, input_acao, input_strike, input_premio):
                input_acao = input_acao.lower()
                input_tipo = input_tipo.lower()
                tipo = ['call', 'put']
                acao=['compra', 'venda']
                if (input_tipo not in tipo) or (input_acao not in acao) :
                    st.error("Ocorreu um erro. Por favor, verifique os campos.")
                    return df
                nova_linha = pd.DataFrame({'Tipo': [f'{input_tipo}'], 'Ação': [f'{input_acao}'], 'Strike (K)': [input_strike], 'Prêmio':[input_premio]})
                df = pd.concat([df,nova_linha])
                return df.reset_index(drop=True)

            

            col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)
            
            with col_1:
                input_tipo = st.text_input("Tipo",placeholder= "Ex: Call", key='acao_input')
            with col_2:
                input_acao = st.text_input("Ação", placeholder= "Ex: Compra", key='tipo_input')
            with col_3:
                input_strike = st.number_input("Strike", value= 80.00, format="%.2f", key='input_strike')
            with col_4:
                input_premio = st.number_input("Premio", value= 10.00, format="%.2f", key='input_premio')
            with col_5:
                if st.button('Adicionar'):
                    st.session_state.df_options = adicionar_linha(st.session_state.df_options, input_tipo, input_acao, input_strike, input_premio)            
            with col_6:
                if st.button('Limpar', type="primary"):
                    st.session_state.df_options = pd.DataFrame()

            if not st.session_state.df_options.empty:
                delete_row = st.checkbox("Deletar alguma linha?")
                if delete_row:
                    row = st.number_input("Escolha a linha a ser deletada",
                                        min_value=0,
                                        max_value=len(st.session_state.df_options)-1)
                    st.markdown(f"Tem certeza que deseja deletar a linha {row}?")
                    if st.button('Deletar', type="primary"):
                        st.session_state.df_options.drop(row, inplace=True)
                        st.session_state.df_options.reset_index(drop=True, inplace=True)
                        st.markdown(f"Linha {row} deletada!")

                st.dataframe(
                    st.session_state.df_options, 
                    use_container_width=True,
                    column_config={
                        'Strike (K)': st.column_config.NumberColumn(
                            format= "%.2f"
                        ),
                        'Prêmio': st.column_config.NumberColumn(
                            format= "%.2f"
                        )
                    })
        
        with col2:
            col__1, col__2, col__3 = st.columns(3)
            with col__1:
                values = st.slider(
                'Intervalo do Ativo Objeto',
                0, 300, (0, 150), key=20)
            with col__2:
                add_papel = st.checkbox("Adicionar o papel?")

            
            S = np.linspace(values[0],values[1], values[1]-values[0]+1)

            if not st.session_state.df_options.empty:
                payoff = 0
                estruturas = []
                strikes = []
                idxs = []
                custo = 0

                for idx, row in st.session_state.df_options.iterrows():
                    payoff = payoff + generate_option(S, row['Strike (K)'], row['Tipo'], row['Ação'], row['Prêmio'])
                    estruturas.append(generate_option(S, row['Strike (K)'], row['Tipo'], row['Ação'], row['Prêmio']))
                    strikes.append(row['Strike (K)'])
                    idxs.append(idx)
                    if row['Ação'] == 'compra':
                        custo = custo - row['Prêmio']
                    else: 
                        custo = custo + row['Prêmio']

                if add_papel:
                    payoff = payoff+S
                    estruturas.append(S)

                with col__3:
                    st.markdown("Financeiro da estrutura:")
                    if custo >= 0:
                        st.markdown(f"+ R${custo}")
                    else:
                        st.markdown(f"- R${custo}")

                st.markdown(f'<h3 style="text-align: center;">Payoff Estrutura</h3>', unsafe_allow_html=True)

                with st.container(border=True):
                
                    fig_estrutura = go.Figure()

                    # Adicionando linhas ao gráfico
                    fig_estrutura.add_trace(go.Scatter(x=S, y=payoff, mode='lines', name='Estrutura', line=dict(color='green')))
                    show_options = st.checkbox("Mostrar composição", key=21)
                    if show_options:
                        for estrutura in estruturas:
                            fig_estrutura.add_trace(go.Scatter(x=S, y=estrutura, mode='lines', line=dict(color='darkgrey', dash='dash')))

                    for i in idxs:
                        fig_estrutura.add_vline(x=strikes[i], line_dash='dash', line_color='blue', line_width=1)
                    

                        fig_estrutura.add_annotation(
                            x=strikes[i],
                            y=0,  # Posição y da anotação
                            text=f'K{i}',
                            showarrow=True,
                            arrowhead=1,
                            font=dict(
                                family='Arial',
                                size=12,
                                color='blue'
                            ),
                        )

                        fig_estrutura.update_layout(
                            xaxis_title='Ativo Objeto no Vencimento',
                            yaxis_title='PnL',
                            legend=dict(
                                orientation='h',  # horizontal
                                y=1.1,  # posicionar a legenda acima do gráfico
                                x=0.5,  # centralizar a legenda
                                xanchor='center',
                                bgcolor='rgba(255, 255, 255, 0)',  # tornar o fundo da legenda transparente
                                bordercolor='rgba(255, 255, 255, 0)'  # tornar a borda da legenda transparente
                            ),
                            autosize=True,
                        )

                    st.plotly_chart(fig_estrutura, use_container_width=True)

if __name__ == "__main__":
    main()
