import React from "react";
import {Products} from './Products';


export class Home extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            products: [],
            fetch_filter: 'products'
        };
        this.updatePage = this.updatePage.bind(this);
        this.fetchProducts = this.fetchProducts.bind(this);
        this.currentPage = 1;
        this.pageTitle = 'Best products from China'
    }

    fetchProducts() {
        fetch(`/api/${this.state.fetch_filter}`)
            .then(response => response.json())
            .then(data => this.setState({
                products: data.results,
                prev: data.previous,
                next: data.next
            }))
    }

    componentDidMount() {
        this.fetchProducts();
        document.title = this.pageTitle;
    }


    updatePage(pageNum) {
        const pageUrl = `/api/${this.state.fetch_filter}?page=${pageNum}`;
        this.currentPage = pageNum;
        fetch(pageUrl)
            .then(response => response.json())
            .then(data => this.setState({
                products: data.results,
                prev: data.previous,
                next: data.next
            }))
    }

    render() {
        return <Products
            products={this.state.products}
            prev={this.state.prev}
            next={this.state.next}
            updatePage={this.updatePage}
            currentPage={this.currentPage}
        />
    }
}
