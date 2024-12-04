from rasters import Raster

from .tiled_granule import ECOSTRESSTiledGranule

class L3TSEB(ECOSTRESSTiledGranule):
    _PRIMARY_VARIABLE = "Rn"
    _PRODUCT_NAME = "L3T_SEB"

    @property
    def Rn(self) -> Raster:
        return self.variable("Rn")
