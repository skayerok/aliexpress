import React from 'react';
import ReactDom from 'react-dom';
import { BrowserRouter } from 'react-router-dom';

import { Header, Main } from "./Core";
import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../css/styles.less';


class App extends React.Component {
    render() {
        return (
            <div>
                <Header />
                <Main />
            </div>
        )
    }
}

ReactDom.render((
    <BrowserRouter>
        <App/>
    </BrowserRouter>
    ), document.getElementById('react')
);
