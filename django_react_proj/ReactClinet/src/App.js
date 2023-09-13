import React, { Component } from "react";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      productList: [],
    };
  }

  componentDidMount() {
    this.refreshList();
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

  render() {
    return (
      <div className="container">
        <h1>Product List</h1>
        <ul>
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
      </div>
    );
  }
}

export default App;
