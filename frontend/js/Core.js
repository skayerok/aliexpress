import React from "react";
import { Link, Switch, Route } from 'react-router-dom';

import { SingleProduct } from "./SingleProduct";
import { Home } from "./Home";
import {CategoriesContainer, CategoryProducts} from "./Categories";


export const Header =() => (
    <header className='container'>
        <div className='row'>
            <Link to='/' className='col-3'>
                <img src="/static/img/sale-logo.png" alt="logo" className='header-logo' />
            </Link>
        </div>
        <div className="row">
            <div className='col-lg-9 col-xs-12 text-center'>
                <h1>Best products from China!</h1>
                <p className='text-muted'>Free shipping, fast check out</p>
            </div>
            <div className="col-3 d-md-none"></div>
        </div>
    </header>
);


export class Main extends React.Component {
    render() {
        return (
            <main className='container'>
                <div className='row'>
                    <Switch>
                        <Route exact path='/' component={Home}/>
                        <Route path='/p/:ali_id' component={SingleProduct}/>
                        <Route path='/c/:category_name' component={CategoryProducts}/>
                    </Switch>
                    <Sidebar/>
                </div>
            </main>
        )
    }
}

class Sidebar extends React.Component {
    render() {
        return <div className='col-3 d-none d-lg-block'>
                <CategoriesContainer/>
            </div>
    }
}
