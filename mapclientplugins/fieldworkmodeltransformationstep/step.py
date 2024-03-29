'''
MAP Client Plugin Step
'''

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint


class FieldworkModelTransformationStep(WorkflowStepMountPoint):
    '''
    Step for applying a rigid-body or scaling transform to
    a fieldwork model.
    '''

    def __init__(self, location):
        super(FieldworkModelTransformationStep, self).__init__('Fieldwork Model Transformation', location)
        self._configured = True  # A step cannot be executed until it has been configured.
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
                        'rigid_about_point': self.GF.transformRigidRotateAboutP,
                        'rigidscale_about_point': self.GF.transformRigidScaleRotateAboutP,
                        }
        try:
            transformFunction = GFTransforms[self.T.transformType]
        except KeyError:
            raise RuntimeError('unknown transform type: ' + self.T.transformType)

        if self.T.transformType == 'affine':
            transformFunction(self.T.T)
        else:
            transformFunction(self.T.getT(), self.T.getP())
        self._doneExecution()

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 0:
            self.GF = dataIn  # ju#fieldworkmodel
        else:
            self.T = dataIn  # ju#geometrictransform

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        return self.GF  # ju#fieldworkmodel

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
        return 'fieldworkmodeltransformation'  # TODO: The string must be replaced with the step's unique identifier

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        pass  # TODO: Must actually set the step's identifier here

    def serialize(self):
        '''
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        '''
        return ''

    def deserialize(self, string):
        '''
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        '''
        pass
