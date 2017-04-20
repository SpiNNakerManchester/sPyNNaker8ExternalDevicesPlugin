from spynnaker8.utilities.data_holder import DataHolder
from spynnaker_external_devices_plugin.pyNN import \
    PushBotSpiNNakerLinkMotorDevice


class PushBotSpiNNakerLinkMotorDeviceDataHolder(DataHolder):
    """ The motor of a PushBot
    """

    def __init__(
            self, motor, protocol, spinnaker_link_id,
            label=PushBotSpiNNakerLinkMotorDevice.default_parameters['label'],
            board_address=PushBotSpiNNakerLinkMotorDevice
            .default_parameters['board_address']):
        """

        :param motor: a PushBotMotor value to indicate the motor to control
        :param protocol: The protocol used to control the device
        :param spinnaker_link_id: The SpiNNakerLink connected to
        :param label: The label of the device
        :param board_address:\
            The IP address of the board that the device is connected to
        """

        DataHolder.__init__(
            self,
            {'motor': motor, 'protocol': protocol,
             'spinnaker_link_id': spinnaker_link_id, 'label': label,
             'board_address': board_address})

    @staticmethod
    def build_model():
        return PushBotSpiNNakerLinkMotorDevice
