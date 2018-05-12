import React from 'react';
import { Link } from 'react-router-dom';
import { Pagination } from "./Pagination";


export class CollectionProduct extends React.Component {
    render() {
        const product_url = `/p/${this.props.ali_id}`;
        return (
            <div className='col-xl-4 col-md-6 col-xs-12 mb-3'>
                <div className='card h-100'>
                    <Link to={product_url}>
                        <img className='card-img-top' src={this.props.preview} />
                    </Link>
                    <div className="card-body d-flex flex-column justify-content-between">
                        <div className='mb-2'>
                            <p className='text-center card-text'>{this.props.name}</p>
                        </div>
                        <p className='product-category-link'>
                            Category: <Link to={`/c/${this.props.category.tech_name}`}>
                                <strong>{this.props.category.name}</strong>
                            </Link>
                        </p>
                        <p className='card-text mt-2'>Price: <strong>{this.props.price}$</strong></p>
                    </div>
                    <div className='card-footer d-flex justify-content-between'>
                        <Link className='btn btn-primary' to={product_url}>More info</Link>
                        <a className='btn btn-success' href={`/redirect/${this.props.ali_id}`}>Buy now!</a>
                    </div>
                </div>
            </div>
        )
    }
}

export class Products extends React.Component {
    render() {
        return (
            <div className='col-xs-12 col-lg-9'>
                <div className='row align-content-stretch'>
                    {
                        this.props.products.map(product =>
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
                <Pagination prev={this.props.prev}
                            next={this.props.next}
                            updatePage={this.props.updatePage}
                            currentPage={this.props.currentPage}
                />
            </div>
        )
    }
}
