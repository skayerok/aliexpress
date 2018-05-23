import React from 'react';


export class Pagination extends React.Component {
    constructor(props) {
        super(props);
        this.nextPage = this.nextPage.bind(this);
        this.prevPage = this.prevPage.bind(this);
    }

    nextPage(e) {
        e.preventDefault();
        this.props.updatePage(this.props.currentPage + 1);
    }

    prevPage(e) {
        e.preventDefault();
        this.props.updatePage(this.props.currentPage - 1);
    }

    render() {
        const prev = <button onClick={this.prevPage} disabled={!this.props.prev} className='btn btn-default'>
            Previous
        </button>;
        const next = <button onClick={this.nextPage} disabled={!this.props.next} className='btn btn-default'>
            Next
        </button>;
        return (
            <nav className="d-flex justify-content-between align-items-center col-xl-4 col-md-6 col-xs-12">
                {prev}
                {this.props.currentPage}
                {next}
            </nav>
        )
    }
}
