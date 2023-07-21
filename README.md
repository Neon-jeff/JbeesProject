# JbeesProject
Jbees api server with django restframework for RESTFUL services and django channels for websockets connection

**Endpoints**
1.   https://jb-api-7ex7.onrender.com/api/menu/
   this endpoint accepts a GET/POST/PATCH request to retrieve all items in the menu with
   their price, image, name props, from the DB. the POST request allows items to be added to the menu DB.
   the patch request allows for partial update in any field of an item object in the menu DB

2.  https://jb-api-7ex7.onrender.com/api/order/ [GET/POST/ ]
    list out all the order made from the frontend and also creates order from the post request

3.  https://jb-api-7ex7.onrender.com/api/order/pk [GET,PUT]
    Update order status

**FRONTEND URL**

   **Landing Page**
   
   https://jbees-menu.vercel.app
   
   **App Entry point**
   
   https://jbees-menu.vercel.app/lounge/1
   
   This is the entry point for the customer to select items and request an order,
   the order is handled and processed by a customised admin panel, built with better
   user friendly features with some extra functionality.
   it also be accessed from scanning the qrcode below
   

![Untitled](https://github.com/Neon-jeff/JbeesProject/assets/101363689/3378efbd-fd9e-4f18-9c30-78a6d7d935ca)
