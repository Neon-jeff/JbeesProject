# JbeesProject
Jbees api server with django restframework,django channels for websockets connection

**Endpoints**
1.   https://jb-api-7ex7.onrender.com/api/menu/
   this endpoint accepts a GET/POST/PATCH request to retrieve all items in the menu with
   their price, image, name props, from the DB. the POST request allows items to be added to the menu DB.
   the patch request allows for partial update in any field of an item object in the menu DB

2.  https://jb-api-7ex7.onrender.com/api/order/ [GET/POST/ ]
    list out all the order made from the frontend and also creates order from the post request

3.  https://jb-api-7ex7.onrender.com/api/order/pk [GET,PUT]
    Update order status


