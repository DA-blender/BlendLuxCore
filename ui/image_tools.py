from bpy.types import Panel
from . import denoiser


class LuxCoreImagePanel:
    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == "LUXCORE"


class LUXCORE_IMAGE_PT_display(Panel, LuxCoreImagePanel):
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_label = "Display"
    bl_category = "LuxCore"

    def draw(self, context):
        layout = self.layout
        display = context.scene.luxcore.display

        layout.prop(display, "refresh", toggle=True, icon="FILE_REFRESH")
        if display.refresh:
            layout.label("Refreshing film...")

        layout.prop(display, "interval")


class LUXCORE_IMAGE_PT_denoiser(Panel, LuxCoreImagePanel):
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_label = "Denoiser"
    bl_category = "LuxCore"

    def draw(self, context):
        denoiser.draw(context, self.layout)