import {
  HashRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import './App.css';
import Header from './components/Header';
import NotesListPage from './Pages/NotesListPage';
import NotePage from './Pages/NotePage'

function App() {
  return (
    <Router>
     
    <div className="container dark">
         <div className="app">
      
            <Header />
            <Routes>
               <Route path='/' element={<NotesListPage/>} />
               <Route path='/notes/:id/' element={<NotePage/>} />
            </Routes>
        </div>
    </div>

    </Router>
   
  );
}

export default App;
