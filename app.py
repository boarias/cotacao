import streamlit as st

def get_best_flight_options(origin, destination):
    """
    Retorna as melhores opções de emissão de passagens com base nos programas de milhas.
    """
    recommendations = {
        # Europa
        ("São Paulo", "Madrid"): [
            {"Cia": "Latam", "Programa": "Latam Pass", "Melhor Rota": "LIS/MAD/LHR/MXP/FRA/BCN/FCO/CDG"},
            {"Cia": "Iberia", "Programa": "Ibéria Plus", "Melhor Rota": "MAD"},
            {"Cia": "AirEuropa", "Programa": "Suma", "Melhor Rota": "MAD"}
        ],
        ("São Paulo", "Paris"): [
            {"Cia": "Air France", "Programa": "Flying Club", "Melhor Rota": "CDG"},
            {"Cia": "Latam", "Programa": "Latam Pass", "Melhor Rota": "LIS/MAD/LHR/MXP/FRA/BCN/FCO/CDG"}
        ],
        ("São Paulo", "Londres"): [
            {"Cia": "British", "Programa": "Ibéria Plus", "Melhor Rota": "LHR"},
            {"Cia": "Latam", "Programa": "Latam Pass", "Melhor Rota": "LIS/MAD/LHR/MXP/FRA/BCN/FCO/CDG"}
        ],
        ("Rio de Janeiro", "Lisboa"): [
            {"Cia": "Tap", "Programa": "Smiles", "Melhor Rota": "LIS"},
            {"Cia": "Tap", "Programa": "Tap", "Melhor Rota": "LIS/OPO (Saídas BEL/FOR/NAT/REC/SSA/BSB/CNF/GIG/GRU/POA)"}
        ],
        ("Brasília", "Frankfurt"): [
            {"Cia": "Lufthansa", "Programa": "Latam Pass", "Melhor Rota": "FRA"},
            {"Cia": "Swiss", "Programa": "Tap", "Melhor Rota": "ZUR"}
        ],
        
        # EUA/Canadá
        ("São Paulo", "Nova York"): [
            {"Cia": "American Airlines", "Programa": "Smiles", "Melhor Rota": "MIA/JFK/DFW"},
            {"Cia": "Latam", "Programa": "Latam Pass", "Melhor Rota": "JFK/MIA/MCO/BOS"}
        ],
        ("São Paulo", "Toronto"): [
            {"Cia": "Air Canada", "Programa": "Smiles", "Melhor Rota": "YYZ/YUL"},
            {"Cia": "Copa Airlines", "Programa": "ConnectMiles", "Melhor Rota": "Via PTY"}
        ],
        
        # América do Sul
        ("São Paulo", "Buenos Aires"): [
            {"Cia": "Latam", "Programa": "Latam Pass", "Melhor Rota": "EZE/SCL"},
            {"Cia": "Air Canada", "Programa": "Smiles", "Melhor Rota": "EZE"}
        ],
        
        # Oriente Médio
        ("São Paulo", "Dubai"): [
            {"Cia": "Emirates", "Programa": "Smiles", "Melhor Rota": "DXB"},
            {"Cia": "Emirates", "Programa": "Tap", "Melhor Rota": "DXB"}
        ],
        
        # Ásia
        ("São Paulo", "Tóquio"): [
            {"Cia": "Qatar", "Programa": "Privilege Club", "Melhor Rota": "Via DOH"},
            {"Cia": "JAL", "Programa": "Latam Pass", "Melhor Rota": "Via EUA"}
        ],
        
        # Oceania
        ("São Paulo", "Sydney"): [
            {"Cia": "Qatar", "Programa": "Latam Pass", "Melhor Rota": "SYD/MEL/ADL/PER (Via DOH)"},
            {"Cia": "Qantas", "Programa": "Latam Pass", "Melhor Rota": "SYD (Via SCL)"}
        ]
    }
    
    return recommendations.get((origin, destination), [])

# Configuração da interface
st.title("Emissor de Passagens com Milhas")
st.write("Digite sua origem e destino para ver as melhores opções de emissão com milhas.")

# Inputs do usuário
origin = st.selectbox("Origem", ["São Paulo", "Rio de Janeiro", "Brasília"])
destination = st.selectbox("Destino", ["Madrid", "Paris", "Londres", "Lisboa", "Frankfurt", "Nova York", "Toronto", "Buenos Aires", "Dubai", "Tóquio", "Sydney"])

if st.button("Buscar Opções"):
    options = get_best_flight_options(origin, destination)
    if options:
        for option in options:
            st.subheader(f"Companhia Aérea: {option['Cia']}")
            st.write(f"Programa de Milhas: {option['Programa']}")
            st.write(f"Melhor Rota: {option['Melhor Rota']}")
            st.markdown("---")
    else:
        st.write("Nenhuma opção encontrada para essa rota.")