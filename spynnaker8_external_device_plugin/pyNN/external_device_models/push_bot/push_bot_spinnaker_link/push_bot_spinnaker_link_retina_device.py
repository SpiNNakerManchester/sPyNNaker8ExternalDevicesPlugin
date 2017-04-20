# pynn imports
from spynnaker8.utilities.data_holder import DataHolder
from spynnaker_external_devices_plugin.pyNN import \
    PushBotSpiNNakerLinkRetinaDevice


class PushBotSpiNNakerLinkRetinaDeviceDataHolder(DataHolder):

    def __init__(
            self, spinnaker_link_id, protocol, resolution,
            board_address=PushBotSpiNNakerLinkRetinaDevice
            .default_parameters['board_address'],
            label=PushBotSpiNNakerLinkRetinaDevice.default_parameters[
                'label']):

        DataHolder.__init__(
            self,
            {'spinnaker_link_id': spinnaker_link_id, 'protocol': protocol,
             'resolution': resolution, 'board_address': board_address,
             'label': label})

    @staticmethod
    def build_model():
        return PushBotSpiNNakerLinkRetinaDevice
