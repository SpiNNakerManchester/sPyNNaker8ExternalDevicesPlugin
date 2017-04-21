from spynnaker8.utilities.data_holder import DataHolder
from spynnaker_external_devices_plugin.pyNN.external_devices_models.push_bot\
    .push_bot_spinnaker_link.push_bot_spinnaker_link_led_device import \
    PushBotSpiNNakerLinkLEDDevice


class PushBotSpiNNakerLinkLEDDeviceDataHolder(DataHolder):
    """ The LED of a PushBot
    """

    def __init__(
            self, led, protocol, spinnaker_link_id,
            label=PushBotSpiNNakerLinkLEDDevice.default_parameters['label'],
            board_address=PushBotSpiNNakerLinkLEDDevice.default_parameters[
                'board_address'],
            start_active_time_front=PushBotSpiNNakerLinkLEDDevice
            .default_parameters['start_active_time_front'],
            start_active_time_back=PushBotSpiNNakerLinkLEDDevice
            .default_parameters['start_active_time_back'],
            start_total_period=PushBotSpiNNakerLinkLEDDevice
            .default_parameters['start_total_period'],
            start_frequency=PushBotSpiNNakerLinkLEDDevice.default_parameters[
                'start_frequency']):
        """

        :param led: The PushBotLED parameter to control
        :param protocol: The protocol instance to get commands from
        :param spinnaker_link_id: The SpiNNakerLink connected to
        :param label: The label of the device
        :param board_address:\
            The IP address of the board that the device is connected to
        :param start_active_time_front:\
            The "active time" to set for the front LED at the start
        :param start_active_time_back:\
            The "active time" to set for the back LED at the start
        :param start_total_period: The "total period" to set at the start
        :param start_frequency: The "frequency" to set at the start
        """
        DataHolder.__init__(
            self,
            {'led': led, 'protocol': protocol,
             'spinnaker_link_id': spinnaker_link_id, 'label': label,
             'board_address': board_address,
             'start_active_time_front': start_active_time_front,
             'start_frequency': start_frequency,
             'start_total_period': start_total_period,
             'start_active_time_back': start_active_time_back})

    @staticmethod
    def build_model():
        return PushBotSpiNNakerLinkLEDDevice
