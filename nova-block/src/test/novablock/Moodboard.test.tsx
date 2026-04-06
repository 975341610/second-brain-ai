import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { MoodboardView } from '../../components/moodboard/MoodboardView'

describe('MoodboardView', () => {
  it('should render the weekly grid (Monday to Sunday)', () => {
    render(<MoodboardView />)
    
    const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    days.forEach(day => {
      expect(screen.getByText(new RegExp(day, 'i'))).toBeDefined()
    })
  })

  it('should have a full-width notes area', () => {
    render(<MoodboardView />)
    expect(screen.getByPlaceholderText(/Write your creative reflection here/i)).toBeDefined()
  })
})
