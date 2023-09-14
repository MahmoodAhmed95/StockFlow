import React, { Component } from "react";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      productList: [],
      categoriesList:[],
      customerList:[],
      vendorList:[],
      saleOrderList:[],
      saleOrderLineList:[],
      purchaseOrderList:[],
      purchaseOrderLineList:[],
    };
  }

  componentDidMount() {
    this.refreshList();
    this.refreshCatList();
    this.refreshCustomerList();
    this.refreshVendorList();
    this.refreshPurchaseList();
    this.refreshPurchaseLineList();
    this.refreshSaleList();
    this.refreshSaleLineList();
  }

  refreshList = () => {
    axios.get("http://localhost:8000/api/products").then((res) => {
      this.setState({ productList: res.data });
    }).catch((err) => {
      if (err.response) {
        // The request was made, but the server responded with an error status
        console.error("Server responded with status code:", err.response.status);
      } else if (err.request) {
        // The request was made, but no response was received
        console.error("No response received from the server");
      } else {
        // Something happened in setting up the request
        console.error("Error:", err.message);
      }
    });};

    refreshCatList = () => {
      axios.get("http://localhost:8000/api/categories").then((res) => {
        this.setState({ categoriesList: res.data });
      }).catch((err) => {
        if (err.response) {
          // The request was made, but the server responded with an error status
          console.error("Server responded with status code:", err.response.status);
        } else if (err.request) {
          // The request was made, but no response was received
          console.error("No response received from the server");
        } else {
          // Something happened in setting up the request
          console.error("Error:", err.message);
        }
      });};
      refreshCustomerList = () => {
        axios.get("http://localhost:8000/api/customer").then((res) => {
          this.setState({ customerList: res.data });
        }).catch((err) => {
          if (err.response) {
            // The request was made, but the server responded with an error status
            console.error("Server responded with status code:", err.response.status);
          } else if (err.request) {
            // The request was made, but no response was received
            console.error("No response received from the server");
          } else {
            // Something happened in setting up the request
            console.error("Error:", err.message);
          }
        });};
        refreshVendorList = () => {
          axios.get("http://localhost:8000/api/vendor").then((res) => {
            this.setState({ vendorList: res.data });
          }).catch((err) => {
            if (err.response) {
              // The request was made, but the server responded with an error status
              console.error("Server responded with status code:", err.response.status);
            } else if (err.request) {
              // The request was made, but no response was received
              console.error("No response received from the server");
            } else {
              // Something happened in setting up the request
              console.error("Error:", err.message);
            }
          });};
          refreshPurchaseList = () => {
            axios.get("http://localhost:8000/api/purchaseorderline").then((res) => {
              this.setState({ purchaseOrderList: res.data });
            }).catch((err) => {
              if (err.response) {
                // The request was made, but the server responded with an error status
                console.error("Server responded with status code:", err.response.status);
              } else if (err.request) {
                // The request was made, but no response was received
                console.error("No response received from the server");
              } else {
                // Something happened in setting up the request
                console.error("Error:", err.message);
              }
            });};
            refreshPurchaseLineList = () => {
              axios.get("http://localhost:8000/api/purchaseorderline").then((res) => {
                this.setState({ purchaseOrderLineList: res.data });
              }).catch((err) => {
                if (err.response) {
                  // The request was made, but the server responded with an error status
                  console.error("Server responded with status code:", err.response.status);
                } else if (err.request) {
                  // The request was made, but no response was received
                  console.error("No response received from the server");
                } else {
                  // Something happened in setting up the request
                  console.error("Error:", err.message);
                }
              });};
              refreshSaleList = () => {
                axios.get("http://localhost:8000/api/saleorder").then((res) => {
                  this.setState({ saleOrderList: res.data });
                }).catch((err) => {
                  if (err.response) {
                    // The request was made, but the server responded with an error status
                    console.error("Server responded with status code:", err.response.status);
                  } else if (err.request) {
                    // The request was made, but no response was received
                    console.error("No response received from the server");
                  } else {
                    // Something happened in setting up the request
                    console.error("Error:", err.message);
                  }
                });};
                refreshSaleLineList = () => {
                  axios.get("http://localhost:8000/api/saleorderline").then((res) => {
                    this.setState({ saleOrderLineList: res.data });
                  }).catch((err) => {
                    if (err.response) {
                      // The request was made, but the server responded with an error status
                      console.error("Server responded with status code:", err.response.status);
                    } else if (err.request) {
                      // The request was made, but no response was received
                      console.error("No response received from the server");
                    } else {
                      // Something happened in setting up the request
                      console.error("Error:", err.message);
                    }
                  });};

  render() {
    return (
      <div className="container">
        <a href="//localhost:8000"> Inventory Management</a>
        <h1>Product List</h1>
        <ul style={{ display:'flex'}}>
          {this.state.productList.map((product) => (
            <li key={product.id}>
              <img src={product.image} alt="proimg" style={{ width: '200px', height: '200px' }}/>
              <h2>{product.name}</h2>
              <p>Purchase Cost: {product.purchaseCost}</p>
              <p>Sale Price: {product.salePrice}</p>
              <p>Product Category: {product.categoryId}</p>
              {/* Add more product information here */}
            </li>
          ))}
        </ul>
        <h1>Categories List</h1>
        <ul style={{ display:'flex'}}>
          {this.state.categoriesList.map((category) => (
            <li key={category.id}>
              <img src={category.image} alt="catimg" style={{ width: '200px', height: '200px' }}/>
              <h2>{category.name}</h2>
              {/* Add more product information here */}
            </li>
          ))}
        </ul>
        <h1>Customer List</h1>
        <ul style={{ display:'flex'}}>
          {this.state.customerList.map((customer) => (
            <li key={customer.id}>
              <h2>{customer.name}</h2>
              <p>Phone: {customer.phone}</p>
              <p>Email: {customer.email}</p>
              {/* Add more product information here */}
            </li>
          ))}
        </ul>
        <h1>vendor List</h1>
        <ul style={{ display:'flex'}}>
          {this.state.vendorList.map((vendor) => (
            <li key={vendor.id}>
              <h2>{vendor.name}</h2>
              <p>Phone: {vendor.phone}</p>
              <p>Email: {vendor.email}</p>
              {/* Add more product information here */}
            </li>
          ))}
        </ul>
        <h1>Purchase Order List</h1>
        <ul style={{ display:'flex'}}>
          {this.state.purchaseOrderList.map((purchase) => (
            <li key={purchase.id}>
              <h2>{purchase.purchaseNote}</h2>
              <p>Purchase Date: {purchase.purchaseDate}</p>
              <p>Purchase Confirm: {purchase.confirmed}</p>
              <p>Vendor Name: {purchase.vendorId}</p>
              {/* Add more product information here */}
            </li>
          ))}
        </ul>
        <h1>Purchase Order Line List</h1>
        <ul style={{ display:'flex'}}>
          {this.state.purchaseOrderLineList.map((purchaseLine) => (
            <li key={purchaseLine.id}>
              <h2>{purchaseLine.productId}</h2>
              <p>Purchase Quantity: {purchaseLine.quantity}</p>
              <p>Purchase ID: {purchaseLine.purchaseId}</p>
              {/* Add more product information here */}
            </li>
          ))}
        </ul>
        <h1>Sale Order List</h1>
        <ul style={{ display:'flex'}}>
          {this.state.saleOrderList.map((sale) => (
            <li key={sale.id}>
              <h2>{sale.saleNote}</h2>
              <p>Sale Date: {sale.saleDate}</p>
              <p>Sale Confirm: {sale.confirmed}</p>
              <p>Customer ID: {sale.customerId}</p>
              {/* Add more product information here */}
            </li>
          ))}
        </ul>
        <h1>Sale Order Line List</h1>
        <ul style={{ display:'flex'}}>
          {this.state.saleOrderLineList.map((saleLine) => (
            <li key={saleLine.id}>
              <h2>{saleLine.productId}</h2>
              <p>Sale Quantity: {saleLine.quantity}</p>
              <p>Sale ID: {saleLine.saleId}</p>
              {/* Add more product information here */}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default App;
