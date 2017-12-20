import bpy
from bpy.props import BoolProperty
from ..output import LuxCoreNodeOutput, update_active


class LuxCoreNodeMatOutput(LuxCoreNodeOutput):
    """
    Material output node.
    This is where the export starts (if the output is active).
    """
    bl_label = "Material Output"
    bl_width_min = 160

    active = BoolProperty(name="Active", default=True, update=update_active)

    def init(self, context):
        self.inputs.new("LuxCoreSocketMaterial", "Material")
        super().init(context)

    def export(self, props, luxcore_name):
        self.inputs["Material"].export(props, luxcore_name)