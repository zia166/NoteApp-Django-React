import React , { useState, useEffect } from 'react'
import AddButton from '../components/AddButton';
import Listitem from '../components/Listitem';


const NotesListPage = () => {

  let [notes, setNotes] = useState([])

  useEffect(()=>{
    getNotes()
  },[])

  let getNotes = async () => {

          let response = await fetch('api/notes/')
          let data = await response.json()
          setNotes(data)
  }

  return (
    <div className='notes'>
      
       <div className='notes-header'>
           <h2 className='notes-title'>&#9782;Notes List</h2>
           <p className='notes-count'>{notes.length}</p>
       </div>
       
       <AddButton/>

       <div className='notes-list'>
              {notes.map((note,index) => (
                 <Listitem key={index} note={note}/> 
              ))}
       </div>
    </div>
  );
}

export default NotesListPage
