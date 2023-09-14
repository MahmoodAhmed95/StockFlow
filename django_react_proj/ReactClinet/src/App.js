import React, { Component } from "react";
import axios from "axios";

import {
  Container,
  Typography,
  Grid,
  Card,
  CardContent,
  CardMedia,
  Button,
  Box,
  IconButton,
  List,
  ListItem,
  ListItemText,
  Paper,
  AppBar,
  Toolbar,
  Link,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import RemoveIcon from "@mui/icons-material/Remove";
import { ThemeProvider, createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#1b2950"
    },
   secondary: {
    main: "#ff9e43"
   }
  },
});
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      productList: [],
      cart: [],
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("http://localhost:8000/api/products")
      .then((res) => {
        this.setState({ productList: res.data });
      })
      .catch((err) => {
        if (err.response) {
          console.error("Server responded with status code:", err.response.status);
        } else if (err.request) {
          console.error("No response received from the server");
        } else {
          console.error("Error:", err.message);
        }
      });
  };

  addToCart = (item) => {
    const { cart } = this.state;
    const existingItem = cart.find((cartItem) => cartItem.id === item.id);

    if (existingItem) {
      const updatedCart = cart.map((cartItem) =>
        cartItem.id === item.id
          ? { ...cartItem, qty: cartItem.qty + 1 }
          : cartItem
      );
      this.setState({ cart: updatedCart });
    } else {
      this.setState({ cart: [...cart, { ...item, qty: 1 }] });
    }
  };

  removeFromCart = (item) => {
    const { cart } = this.state;
    const existingItem = cart.find((cartItem) => cartItem.id === item.id);

    if (existingItem) {
      if (existingItem.qty > 1) {
        const updatedCart = cart.map((cartItem) =>
          cartItem.id === item.id
            ? { ...cartItem, qty: cartItem.qty - 1 }
            : cartItem
        );
        this.setState({ cart: updatedCart });
      } else {
        const updatedCart = cart.filter((cartItem) => cartItem.id !== item.id);
        this.setState({ cart: updatedCart });
      }
    }
  };

  getTotalPrice = () => {
    const { cart } = this.state;
    return cart.reduce(
      (total, cartItem) => total + cartItem.qty * cartItem.salePrice,
      0
    );
  };

  render() {
    return (
      <ThemeProvider theme={theme}>
     
          <Container>
      
            <AppBar position="static" color="primary">
              <Toolbar>
                <Link href="http://localhost:8000" color="inherit">
                  <Typography variant="h6">Main</Typography>
                </Link>
              </Toolbar>
            </AppBar>
    
            <Typography variant="h3" gutterBottom>
              Products
            </Typography>
            <Grid container spacing={2}>
          <Grid item xs={12} md={8}>
            <Grid container spacing={2}>
              {this.state.productList.map((product) => (
                <Grid item xs={12} sm={6} md={4} key={product.id}>
                  <Card>
                    <CardMedia
                      component="img"
                      alt={product.name}
                      height="201"
                      image={product.image}
                    />
                    <CardContent>
                      <Typography variant="h5">{product.name}</Typography>
                      <Typography variant="subtitle1">
                        BHD {product.salePrice}
                      </Typography>
                    </CardContent>
                    <Button
                      variant="contained"
                      color="secondary"
                      onClick={() => this.addToCart(product)}
                    >
                      Add to Cart
                    </Button>
                  </Card>
                </Grid>
              ))}
            </Grid>
          </Grid>
          <Grid item xs={12} md={4}>
            <Paper elevation={3} style={{ padding: 16 }}>
              <Typography variant="h5" gutterBottom>
                Shopping Cart
              </Typography>
              <List>
                {this.state.cart.map((cartItem) => (
                  <ListItem key={cartItem.id}>
                    <ListItemText
                      primary={cartItem.name}
                      secondary={`Qty ${cartItem.qty} - Total BHD ${(
                        cartItem.qty * cartItem.salePrice
                      ).toFixed(2)}`}
                    />
                    <IconButton
                      color="secondary"
                      onClick={() => this.addToCart(cartItem)}
                    >
                      <AddIcon />
                    </IconButton>
                    <IconButton
                      color="secondary"
                      onClick={() => this.removeFromCart(cartItem)}
                    >
                      <RemoveIcon />
                    </IconButton>
                   
                  </ListItem>
                ))}
              </List>
              <Box mt={2}>
                <Typography variant="h6">
                  Total Price: BHD {this.getTotalPrice().toFixed(2)}
                </Typography>
                <Link href="http://localhost:3000" color="inherit">
                <Button
                      variant="contained"
                      color="secondary"
                     
                    >
                      Checkout
                    </Button>
                </Link>
                
              </Box>
            </Paper>
          </Grid>
        </Grid>
      </Container>
      </ThemeProvider>
          
        );
  
  }
}

export default App;
