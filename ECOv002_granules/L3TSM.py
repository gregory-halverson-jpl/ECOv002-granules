from rasters import Raster

from .tiled_granule import ECOSTRESSTiledGranule

class L3TSM(ECOSTRESSTiledGranule):
    _PRIMARY_VARIABLE = "SM"
    _PRODUCT_NAME = "L3T_SM"

    @property
    def SM(self) -> Raster:
        return self.variable("SM")
