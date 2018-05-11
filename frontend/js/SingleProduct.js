import React from 'react';
import { Link } from 'react-router-dom';

export class SingleProduct extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            ali_id: '',
            category_id: '',
            description: '',
            name: '',
            pictures: '',
            preview_url: '',
            url: '',
            category: ''
        }
    }

    componentDidMount() {
        const ali_id = this.props.match.params.ali_id;
        fetch(`/api/product/${ali_id}`)
            .then(response => response.json())
            .then(data => this.setState({
                ali_id: data.ali_id,
                category_id: data.category_id,
                description: data.description,
                name: data.name,
                pictures: data.pictures,
                preview_url: data.preview_url,
                url: data.short_url || data.url,
                category: data.category
            }));
    }

    getImgAlt() {
        return this.state.name.length ? this.state.name.split(' ').slice(0, 4).join(' ') : '';
    }

    render() {
        const description = this.state.description ? <p>{this.state.description}</p> : '';
        const img_alt = this.getImgAlt(this.state.name);
        document.title = this.state.name ? this.state.name : 'Product info';
        return <section className='col-lg-9 col-xs-12'>
            <a href={`/redirect/${this.state.ali_id}`} className='btn btn-success buy-btn'>Buy now</a>
            <h2 className='text-center'>{this.state.name}</h2>
            {description}
            <img className='w-100' src={this.state.preview_url} alt={img_alt} />
            <p className='single-product-category-link'>
                Category: <Link to={`/c/${this.state.category.tech_name}`}>
                    <strong>{this.state.category.name}</strong>
                </Link>
            </p>
            <a href={`/redirect/${this.state.ali_id}`} className='btn btn-success buy-btn mt-2'>Buy now</a>
        </section>
    }
}
