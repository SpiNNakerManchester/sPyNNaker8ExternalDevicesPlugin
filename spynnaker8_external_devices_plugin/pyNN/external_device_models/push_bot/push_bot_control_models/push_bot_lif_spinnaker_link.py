from spynnaker.pyNN.models.neuron.abstract_population_vertex import \
    AbstractPopulationVertex
from spynnaker8.utilities.data_holder import DataHolder
from spynnaker_external_devices_plugin.pyNN.external_devices_models.push_bot\
    .push_bot_control_modules.push_bot_lif_spinnaker_link import \
    PushBotLifSpinnakerLink
from spynnaker_external_devices_plugin.pyNN.external_devices_models\
    .external_device_lif_control import ExternalDeviceLifControl

import logging

logger = logging.getLogger(__name__)


class PushBotLifSpinnakerLinkDataHolder(DataHolder):
    """ Control module for a pushbot connected to a SpiNNaker Link
    """

    def __init__(
            self, protocol, devices,

            spikes_per_second=AbstractPopulationVertex.
            none_pynn_default_parameters['spikes_per_second'],
            label=AbstractPopulationVertex.none_pynn_default_parameters[
                'label'],
            ring_buffer_sigma=AbstractPopulationVertex.
            none_pynn_default_parameters['ring_buffer_sigma'],
            incoming_spike_buffer_size=AbstractPopulationVertex.
            none_pynn_default_parameters['incoming_spike_buffer_size'],
            constraints=AbstractPopulationVertex.
            none_pynn_default_parameters['constraints'],

            # default params for the neuron model type
            tau_m=ExternalDeviceLifControl.default_parameters['tau_m'],
            cm=ExternalDeviceLifControl.default_parameters['cm'],
            v_rest=ExternalDeviceLifControl.default_parameters['v_rest'],
            v_reset=ExternalDeviceLifControl.default_parameters['v_reset'],
            tau_syn_E=ExternalDeviceLifControl.default_parameters['tau_syn_E'],
            tau_syn_I=ExternalDeviceLifControl.default_parameters['tau_syn_I'],
            tau_refrac=ExternalDeviceLifControl.default_parameters[
                'tau_refrac'],
            i_offset=ExternalDeviceLifControl.default_parameters['i_offset'],
            v_init=ExternalDeviceLifControl.none_pynn_default_parameters[
                'v_init']):

        DataHolder.__init__(
            self,
            {'protocol': protocol, 'devices': devices,
             'spikes_per_second': spikes_per_second,
             'ring_buffer_sigma': ring_buffer_sigma, 'label': label,
             'incoming_spike_buffer_size': incoming_spike_buffer_size,
             'constraints': constraints,
             'tau_m': tau_m, 'cm': cm, 'v_rest': v_rest, 'v_reset': v_reset,
             'tau_syn_E': tau_syn_E, 'tau_syn_I': tau_syn_I,
             'tau_refac': tau_refrac, 'i_offset': i_offset, 'v_init': v_init})

    @staticmethod
    def build_model():
        return PushBotLifSpinnakerLink
