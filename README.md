Fieldwork Model Transformation Step
===================================
MAP Client plugin for applying a rigid-body, scaling, or affine transform to a GIAS2 Fieldwork model.

Requires
--------
None

Inputs
------
- **fieldworkmodel** : GIAS2 Fieldwork model (GeometricField instance) to be transformed
- **geometrictransform** : GIAS2 Transformation instance containing the transformation to be applied

Outputs
-------
- **fieldworkmodel** : The transformed GIAS2 Fieldwork model (GeometricField instance).

Configuration
-------------
None

Usage
-----
This step applies a transformation provided by, for example "Pointwise Rigid Registration Step", to a Fieldwork mesh model.
