class Nav1 extends React.Component{
    constructor(props){
        super(props);
      this.state={
       index:0,
      };
      props={
       typecl:['XS','S','M','L','XL']
      };
    }
      render(){
        return <div>
            <nav className="navbar navbar-expand-sm bg-dark navbar-dark">
                <div className="container-fluid">
                  <ul className="nav nav-tabs">
                    {this.props.typecl.map((cl,ind)=>  <li className="nav-item"
                    onClick={()=>{this.state.index=ind;alert(ind);}}   key={cl}>

                        <a className="nav-link active" href="#">{cl}</a>
                      </li>
                        )}
                   </ul>
                </div>
              </nav>
        </div>
      
    }
   }