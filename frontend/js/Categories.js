import React from 'react';
import { Link } from 'react-router-dom';
import { Home } from "./Home";
import { CollectionProduct } from "./Products";
import { Pagination } from "./Pagination";


class Category extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return <li className='list-group-item'>
            <Link to={`/c/${this.props.tech_name}`}>{this.props.name}</Link>
        </li>
    }
}


export class CategoriesContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            categories: []
        };
    }
    componentDidMount() {
        fetch('/api/categories/')
            .then(response => response.json())
            .then(data => this.setState({
                categories: data.results
            }))
    }

    render() {
        return (
            <div className='card text-center'>
                <h2 className='card-header'>Categories</h2>
                <ul className='list-group list-group-flush'>
                    {
                        this.state.categories.map(category =>
                            <Category
                                key={category.category_id}
                                name={category.name}
                                tech_name={category.tech_name}
                            />
                        )
                    }
                </ul>
            </div>
        )
    }
}


export class CategoryProducts extends Home {
    constructor(props) {
        super(props);
        this.category_name = CategoryProducts.getCategoryName(props.match.params.category_name);
        this.state.fetch_filter = `products/${props.match.params.category_name}`;
        this.updateTitle();
    }

    static getCategoryName(tech_name) {
        const categories_map = {
            womens_clothing_and_accessories: "Women's Clothing and Accessories",
            home_appliances: 'Home Appliances',
            computer_and_office: 'Computer and Office',
            home_improvement: 'Home Improvement',
            home_and_garden: 'Home and Garden',
            sports_and_entertainment: 'Sports and Entertainment',
            office_and_school_supplies: 'Office and School Supplies',
            toys_and_hobbies: 'Toys and Hobbies',
            security_and_protection: 'Security and Protection',
            automobiles_and_motorcycles: 'Automobiles and Motorcycles',
            jewelry_and_accessories: 'Jewelry and Accessories',
            lights_and_lighting: 'Lights and Lighting',
            consumer_electronics: 'Consumer Electronics',
            beauty_and_health: 'Beauty and Health',
            weddings_and_events: 'Weddings and Events',
            shoes: 'Shoes',
            electronic_components_and_supplies: 'Electronic Components and Supplies',
            phones_and_telecommunications: 'Phones and Telecommunications',
            tools: 'Tools',
            mother_and_kids: 'Mother and Kids',
            furniture: 'Furniture',
            watches: 'Watches',
            luggage_and_bags: 'Luggage and Bags',
            mens_clothing_and_accessories: "Men's Clothing and Accessories",
            novelty_and_special_use: 'Novelty and Special Use',
            hair_extensions_and_wigs: 'Hair Extensions and Wigs',
            hair_and_accessories: 'Hair and Accessories'
        };
        let category_name = categories_map[tech_name];
        if (!category_name) {
            category_name = tech_name.replace('_', ' ');
        }
        return category_name;
    }

    updateTitle() {
        this.pageTitle = `Best products by category ${this.category_name}`;
    }

    componentWillReceiveProps(nextProps) {
        this.state.fetch_filter = `products/${nextProps.match.params.category_name}`;
        this.category_name = CategoryProducts.getCategoryName(nextProps.match.params.category_name);
        this.updateTitle();
        this.fetchProducts();
    }

    render() {
        document.title = this.pageTitle;
        return (
            <div className='col-xs-12 col-lg-9'>
                <div className='row'>
                    {
                        this.state.products.map(product =>
                            <CollectionProduct key={product.ali_id}
                                               ali_id={product.ali_id}
                                               name={product.name}
                                               preview={product.preview_url}
                                               price={product.price}
                                               category={product.category}
                            />
                        )
                    }

                </div>
                <div className="row justify-content-center">
                    <Pagination prev={this.state.prev}
                                next={this.state.next}
                                updatePage={this.updatePage}
                                currentPage={this.currentPage}
                    />
                </div>
            </div>
        )
    }
}
