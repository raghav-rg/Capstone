from simulation.ema_macd import run_ema_macd
from simulation.ma_cross import run_ma_sim
from infrastructure.collect_data import run_collection
from openfx_api.openfx_api import OpenFxApi


from infrastructure.instrument_collection import instrumentCollection

if __name__ == "__main__":
    
    api = OpenFxApi()

    instrumentCollection.LoadInstruments("./data")
    
    # run_collection(instrumentCollection, api)
    
    
    run_ma_sim()
    run_ema_macd(instrumentCollection)