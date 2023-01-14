import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


dpg.create_context()

# add a font registry
with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("./assets/Ubuntu-Regular.ttf", 16)

dpg.create_viewport(title='Custom Title', width=600, height=600)

dpg.bind_font(default_font)

demo.show_demo()

dpg.set_primary_window("__demo_id",True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
