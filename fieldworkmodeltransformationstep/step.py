
'''
MAP Client Plugin Step
'''

from PySide import QtGui

from mountpoints.workflowstep import WorkflowStepMountPoint

from mappluginutils.datatypes import transformations


class fieldworkmodeltransformationStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(fieldworkmodeltransformationStep, self).__init__('Fieldwork Model Transformation', location)
        self._configured = True # A step cannot be executed until it has been configured.
        self._category = 'Fieldwork'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#fieldworkmodel'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#geometrictransform'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#fieldworkmodel'))

        self.GF = None
        self.T = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        GFTransforms = {'affine': self.GF.transformAffine,
                        'rigid':  self.GF.transformRigidRotateAboutCoM,
                        'rigidScale': self.GF.transformRigidScale3DAboutCoM,
                        }
        try:
            transformFunction = GFTransforms[self.T.transformType]
        except KeyError:
            raise RuntimeError, 'unknown transform type: '+self.T.transformType

        transformFunction(self.T.T)
        self._doneExecution()

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 0:
            self.GF = dataIn # ju#fieldworkmodel
        else:
            self.T = dataIn # ju#geometrictransform

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        return self.GF # ju#fieldworkmodel

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        pass

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return 'fieldworkmodeltransformation' # TODO: The string must be replaced with the step's unique identifier

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        pass # TODO: Must actually set the step's identifier here

    def serialize(self, location):
        '''
        Add code to serialize this step to disk.  The filename should
        use the step identifier (received from getIdentifier()) to keep it
        unique within the workflow.  The suggested name for the file on
        disk is:
            filename = getIdentifier() + '.conf'
        '''
        pass

    def deserialize(self, location):
        '''
        Add code to deserialize this step from disk.  As with the serialize 
        method the filename should use the step identifier.  Obviously the 
        filename used here should be the same as the one used by the
        serialize method.
        '''
        pass

