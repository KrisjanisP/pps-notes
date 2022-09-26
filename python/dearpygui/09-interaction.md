## Atzvani
Callbacks give items functionality by assigning a function to run when they are activated and almost all UI Items in DPG can run callbacks.

Functions or methods are assigned as UI item callbacks when an item is created or at a later runtime using set_item_callback

Callbacks may have up to 3 arguments in the following order.

sender:
the id of the UI item that submitted the callback

app_data:
occasionally UI items will send their own data (ex. file dialog)

user_data:
any python object you want to send to the function

## Elementu vērtības

Almost all UI items have a value which can be accessed or set.

All UI items that have a value also have the default_value parameter which will set the items’ initial starting value.

Values can be accessed using get_value.

Below is an example of setting the default_value for two different items, setting a callback to the items and printing their values.

An input item’s value is changed by interacting with it. In the above example, moving slider_float1 slider to 30.55 sets its’ value to 30.55.

We can set the position of the slider by changing items’ value at runtime using set_value.

The values’ type depends on the widget. (ex.) input_int default value needs to be an integer.

## Apstrādātāju izmantošana

UI item handlers listen for events (changes in state) related to a UI item then submit a callback.
