import React from 'react'
import { Link } from 'react-router-dom'
// import { ReactComponent as AddIcon  } from '../assets/addbutton.svg'
const AddButton = () => {
  return (
    <Link to="/notes/new/" className='floating-button'>
      {/* <AddIcon /> */}
      <p>Add Note </p>
    </Link>
  )
}

export default AddButton
