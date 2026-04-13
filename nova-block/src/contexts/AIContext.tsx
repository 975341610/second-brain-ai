import React, { createContext, useContext, useState, useEffect } from 'react';
import { api } from '../lib/api';

interface AIContextType {
  isAiEnabled: boolean;
  setIsAiEnabled: (enabled: boolean) => void;
  refreshAiStatus: () => Promise<void>;
}

const AIContext = createContext<AIContextType | undefined>(undefined);

export const AIProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [isAiEnabled, setIsAiEnabled] = useState(false);

  const refreshAiStatus = async () => {
    try {
      const status = await api.getAIPluginStatus();
      setIsAiEnabled(status.enabled);
    } catch (err) {
      console.error('Failed to fetch AI status:', err);
    }
  };

  useEffect(() => {
    refreshAiStatus();
  }, []);

  return (
    <AIContext.Provider value={{ isAiEnabled, setIsAiEnabled, refreshAiStatus }}>
      {children}
    </AIContext.Provider>
  );
};

export const useAI = () => {
  const context = useContext(AIContext);
  if (context === undefined) {
    throw new Error('useAI must be used within an AIProvider');
  }
  return context;
};
