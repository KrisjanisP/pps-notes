import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Tutorial"):
    b0 = dpg.add_button(label="button 0")
    b1 = dpg.add_button(tag=100, label="button 1")
    dpg.add_button(tag="btn2", label="button 2")

print(b0, dpg.get_item_label(b0))
print(b1, dpg.get_item_label(b1))
print("btn2", dpg.get_item_label("btn2"))

dpg.create_viewport(title="Custom Title", width=600, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
