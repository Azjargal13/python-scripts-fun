sample_sensor_data = {'photoSensor': 1,
                 'channels':
                 {'channel2': 0.0,
                  'channel6': 2.352941316716828,
                  'channel7': 2.352941316716828,
                  'channel3': 2.352941316716828,
                  'channel0': 1.7881395564245649e-06,
                  'channel4': 2.352941316716828,
                  'channel1': 0.588235329179207,
                  'channel5': 2.352941316716828},
                 'timestamp': '2019-06-05T01:26:55.489+00:00'}

print(sample_sensor_data['channels'])

''' test for retrieve sensor manager module '''

from retrieveSensorData.retrieveSensorManager import RetrieveSensorManager
from retrieveSensorData.cycleStatus import Status

from unittest.mock import patch
import pytest

sample_sensor_data = {'photoSensor': 1,
                 'channels':
                 {'channel2': 0.0,
                  'channel6': 2.352941316716828,
                  'channel7': 2.352941316716828,
                  'channel3': 2.352941316716828,
                  'channel0': 1.7881395564245649e-06,
                  'channel4': 2.352941316716828,
                  'channel1': 0.588235329179207,
                  'channel5': 2.352941316716828},
                 'timestamp': '2019-06-05T01:26:55.489+00:00'}

sample_cycle_status = {
    Status.Started,
    Status.InProgress,
    Status.Finished,
    Status.Timeout,
    Status.Idle,
}

sample_sensor_data_invalid = {}
sample_cycle_status_invalid = {}
@patch('retrieveSensorData.retrieveSensorManager.BufferStorage')
@patch('retrieveSensorData.retrieveSensorManager.CycleStatus', return_value = sample_cycle_status)
@patch('retrieveSensorData.retrieveSensorManager.CSVFileCreation')
@patch('retrieveSensorData.retrieveSensorManager.DataManager', return_value = sample_sensor_data)


class Test_RetrieveSensorManager():
    def test_run(self, mock_Buffer, mock_CycleStatus, mock_CSV, mock_DataManager, tmpdir):
        counter = 2
        outdir = tmpdir
        isPullUp = False
        retrieveSensorManager = RetrieveSensorManager(counter, outdir, isPullUp)
        retrieveSensorManager.retrieveData = mock_DataManager()
        retrieveSensorManager.cycleStatus = mock_CycleStatus()
        retrieveSensorManager.cycleStatus = mock_CycleStatus.return_value
        retrieveSensorManager.bufferStorage = mock_Buffer()
        retrieveSensorManager.csvFileCreation = mock_CSV()
        retrieveSensorManager.run()
        mock_Buffer.assert_called_with()
        mock_CycleStatus.assert_called_with()
        mock_CSV.assert_called_with()
        mock_DataManager.assert_called_with()

    def test_run_exception(self, mock_Buffer, mock_CycleStatus, mock_CSV, mock_DataManager, tmpdir):
        counter = 2
        outdir = tmpdir
        isPullUp = False
        retrieveSensorManager = RetrieveSensorManager(counter, outdir, isPullUp)
        retrieveSensorManager.retrieveData = mock_DataManager.return_value = sample_sensor_data_invalid
        retrieveSensorManager.cycleStatus = mock_CycleStatus()
        retrieveSensorManager.cycleStatus = mock_CycleStatus.return_value = sample_cycle_status_invalid
        retrieveSensorManager.bufferStorage = mock_Buffer()
        retrieveSensorManager.csvFileCreation = mock_CSV()
        with pytest.raises(Exception) as e.info:
            retrieveSensorManager.run()
        mock_Buffer.assert_called_with()
        mock_CycleStatus.assert_called_with()
        mock_CSV.assert_called_with()
        mock_DataManager.assert_called_with()

