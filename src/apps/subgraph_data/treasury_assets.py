from src.apps.subgraph_data.protocol_metrics import get_bct_treasury, \
    get_df_for_treasury_asset_by_address

from src.apps.util.constants import BCT_ERC20_CONTRACT, BCT_USDC_PAIR, \
     KLIMA_BCT_PAIR, KLIMA_MCO2_PAIR, KLIMA_USDC_PAIR, \
     MCO2_ERC20_CONTRACT, NBO_ERC20_CONTRACT, \
     NCT_ERC20_CONTRACT, UBO_ERC20_CONTRACT, USDC_ERC20_CONTRACT

from subgrounds.plotly_wrappers import Scatter

MODE_ASSET_VALUE_IN_USD = "mode_usd"
MODE_CARBON_CUSTODIED = "mode_carbon_custodied"


class TreasuryAssetWrapper:
    def __init__(self, mode):
        self.mode = mode
        treasuryAssetData = []
        treasuryAssetData.append(SingleAssetData(
            name="BCT", address=BCT_ERC20_CONTRACT, color="#eff542", custodiesCarbon=True))
        treasuryAssetData.append(SingleAssetData(
            "KLIMA BCT LP", KLIMA_BCT_PAIR, "#f1c232", True))
        treasuryAssetData.append(SingleAssetData(
            "BCT USDC LP", BCT_USDC_PAIR, "#bf9000", False))
        treasuryAssetData.append(SingleAssetData(
            "MCO2", MCO2_ERC20_CONTRACT, "#93c47d", True))
        treasuryAssetData.append(SingleAssetData(
            "KLIMA MCO2 LP", KLIMA_MCO2_PAIR, "#6aa84f", True))
        treasuryAssetData.append(SingleAssetData(
            "USDC", USDC_ERC20_CONTRACT, "#e06666", False))
        treasuryAssetData.append(SingleAssetData(
            "KLIMA USDC LP", KLIMA_USDC_PAIR, "#cc0000", False))
        treasuryAssetData.append(SingleAssetData(
            "UBO", UBO_ERC20_CONTRACT, "#c27ba0", True))
        treasuryAssetData.append(SingleAssetData(
            "NBO", NBO_ERC20_CONTRACT, "#8e7cc3", True))
        treasuryAssetData.append(SingleAssetData(
            "NCT", NCT_ERC20_CONTRACT, "#6fa8dc", True))

        self.asset_data = treasuryAssetData

    def create_scatters(self):
        scatters = []
        for single_asset_data in self.asset_data:
            if self.mode == MODE_ASSET_VALUE_IN_USD:
                scatter = self.create_scatter(
                    single_asset_data,
                    single_asset_data.formatted_market_value)
                scatters.append(scatter)
            elif self.mode == MODE_CARBON_CUSTODIED:
                if single_asset_data.custodiesCarbon:
                    scatter = self.create_scatter(
                        single_asset_data,
                        single_asset_data.carbon_custodied)
                    scatters.append(scatter)

        return scatters

    def create_scatter(self, single_asset_data, y_data):
        return Scatter(
                name=single_asset_data.name,
                x=single_asset_data.datetime,
                y=y_data,
                mode='lines',
                line={'width': 0.5, 'color': single_asset_data.color},
                stackgroup='one',
            )


class SingleAssetData:
    def __init__(self, name, address, color, custodiesCarbon):
        self.name = name
        self.address = address
        self.color = color
        self.custodiesCarbon = custodiesCarbon

        # Scatter requires at least one item that is not a dataframe, seems to be a bug
        if name == 'BCT':
            bct_treasury_asset = get_bct_treasury()
            self.datetime = bct_treasury_asset.datetime
            self.formatted_market_value = bct_treasury_asset.formatted_market_value
            self.carbon_custodied = bct_treasury_asset.carbonCustodied
        else:
            dataframe = get_df_for_treasury_asset_by_address(address)
            self.datetime = dataframe.treasuryAssets_datetime
            self.formatted_market_value = dataframe.treasuryAssets_formatted_market_value
            self.carbon_custodied = dataframe.treasuryAssets_carbonCustodied
        print(self.name + " is initialized")
