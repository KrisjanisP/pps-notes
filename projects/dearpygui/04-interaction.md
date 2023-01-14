## Atzvani

"**Atzvani**" piešķir **saskarnes elementiem** funkciju, kura tiek palaista, kad šie elementi tiek aktivizēti.

Atzvanu iespējams piešķirt ar `set_item_callback(sender, app_data, user_data)`.

```python
def button_callback(sender, app_data, user_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")

dpg.set_item_callback(btn, button_callback)
```

## Elementu vērtības

Gandrīz katram lietotāja **saskarnes elementam** piemīt vērtība, kuru var **nolasīt vai rediģēt**.

Katram elementam, kam piemīt vērtība, piemīt arī **noklusējuma vērtība** `default_value`.
```python
dpg.add_slider_int(default_value=15, tag="slider_int")
```
Vērtības nolasa izmantojot `get_value` metodi.

Vērtības rediģē izmantojot `set_value` metodi.
```python
input_txt2 = dpg.add_input_text(
    label="InputTxt2",
    default_value="This is a default value!",
    callback=print_value
)
print(dpg.get_value(input_txt2))

dpg.set_value(input_txt2, "Hello")
print(dpg.get_value(input_txt2))

```