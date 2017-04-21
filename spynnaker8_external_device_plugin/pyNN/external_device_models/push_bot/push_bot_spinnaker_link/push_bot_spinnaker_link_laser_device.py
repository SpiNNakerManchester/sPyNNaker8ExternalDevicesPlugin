
# pynn imports
from spynnaker8.utilities.data_holder import DataHolder
from spynnaker_external_devices_plugin.pyNN.external_devices_models.push_bot\
    .push_bot_spinnaker_link.push_bot_spinnaker_link_laser_device import \
    PushBotSpiNNakerLinkLaserDevice


class PushBotSpiNNakerLinkLaserDeviceDataHolder(DataHolder):
    """ The Laser of a PushBot
    """

    def __init__(
            self, laser, protocol, spinnaker_link_id,
            label=PushBotSpiNNakerLinkLaserDevice.default_parameters['label'],
            board_address=PushBotSpiNNakerLinkLaserDevice.default_parameters[
                'board_address'],
            start_active_time=PushBotSpiNNakerLinkLaserDevice.
            default_parameters['start_active_time'],
            start_total_period=PushBotSpiNNakerLinkLaserDevice
            .default_parameters['start_total_period'],
            start_frequency=PushBotSpiNNakerLinkLaserDevice
            .default_parameters['start_frequency']):
        """

        :param laser: The PushBotLaser value to control
        :param protocol: The protocol instance to get commands from
        :param spinnaker_link_id:\
            The SpiNNakerLink that the PushBot is connected to
        :param label: A label for the device
        :param board_address:\
            The IP address of the board that the device is connected to
        :param start_active_time: The "active time" value to send at the start
        :param start_total_period:\
            The "total period" value to send at the start
        :param start_frequency: The "frequency" to send at the start
        """

        DataHolder.__init__(
            self,
            {'laser': laser, 'protocol': protocol,
             'spinnaker_link_id': spinnaker_link_id, 'label': label,
             'board_address': board_address,
             'start_active_time': start_active_time,
             'start_total_period': start_total_period,
             'start_frequency': start_frequency})

    @staticmethod
    def build_model():
        return PushBotSpiNNakerLinkLaserDevice
