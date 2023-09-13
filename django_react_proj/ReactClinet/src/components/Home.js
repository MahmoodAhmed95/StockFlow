import React, { useState, useEffect } from 'react';
import {
  Button,
  Container,
  Grid,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
  Typography,
  Box,
} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import RemoveIcon from '@mui/icons-material/Remove';
import axios from "axios";
import { API_URL } from "../constants/index";

function Home() {
  const [cart, setCart] = useState([]);
  const [products, setProducts] = useState([]);

  // Fetch products from the API when the component mounts
  useEffect(() => {
    // Replace 'API_URL' with your actual API URL for fetching products
    axios.get(API_URL)
      .then((response) => {
        setProducts(response.data);
      })
      .catch((error) => {
        console.error('Error fetching products:', error);
      });
  }, []); // The empty dependency array ensures this effect runs only once

  const addToCart = (item) => {
    const existingItem = cart.find((cartItem) => cartItem.id === item.id);

    if (existingItem) {
      setCart((prevCart) =>
        prevCart.map((cartItem) =>
          cartItem.id === item.id
            ? { ...cartItem, qty: cartItem.qty + 1 }
            : cartItem
        )
      );
    } else {
      setCart((prevCart) => [...prevCart, { ...item, qty: 1 }]);
    }
  };

  const removeFromCart = (item) => {
    const existingItem = cart.find((cartItem) => cartItem.id === item.id);

    if (existingItem) {
      if (existingItem.qty > 1) {
        setCart((prevCart) =>
          prevCart.map((cartItem) =>
            cartItem.id === item.id
              ? { ...cartItem, qty: cartItem.qty - 1 }
              : cartItem
          )
        );
      } else {
        setCart((prevCart) => prevCart.filter((cartItem) => cartItem.id !== item.id));
      }
    }
  };

  const totalCartPrice = cart.reduce(
    (total, cartItem) => total + cartItem.qty * cartItem.salePrice,
    0
  );

  return (
    <Container>
      <Typography variant="h3" gutterBottom>
        Products
      </Typography>
      <Grid container spacing={2}>
        {products.map((item) => (
          <Grid item xs={12} sm={6} md={4} key={item.id}>
            <Box border={1} p={2} borderColor="grey.300">
              <Typography variant="h5">{item.name}</Typography>
              <Typography variant="subtitle1">${item.salePrice}</Typography>
              <IconButton color="primary" onClick={() => addToCart(item)}>
                <AddIcon />
              </IconButton>
              <IconButton color="secondary" onClick={() => removeFromCart(item)}>
                <RemoveIcon />
              </IconButton>
            </Box>
          </Grid>
        ))}
      </Grid>

      <Typography variant="h3" gutterBottom mt={3}>
        Shopping Cart
      </Typography>
      <List>
        {cart.map((cartItem) => (
          <ListItem key={cartItem.id}>
            <ListItemText
              primary={cartItem.name}
              secondary={`Qty ${cartItem.qty} - Total $${(cartItem.qty * cartItem.salePrice).toFixed(2)}`}
            />
            <ListItemSecondaryAction>
              <IconButton color="secondary" onClick={() => removeFromCart(cartItem)}>
                <RemoveIcon />
              </IconButton>
            </ListItemSecondaryAction>
          </ListItem>
        ))}
      </List>
      <Typography variant="h5" mt={2}>
        Total Price: ${totalCartPrice.toFixed(2)}
      </Typography>
    </Container>
  );
}

export default Home;
