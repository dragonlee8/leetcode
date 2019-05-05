//author @asad_nitp
#pragma once
namespace Smart_Pointers 
{
class ReferenceCountManager 
{
public:
    ReferenceCountManager():
       m_ref_count(0)
    {}

    void incrementReferenceCount() 
    {
        ++m_ref_count;
    }

    int decrementReferenceCount() 
    {
        return --m_ref_count;
    }

    int getReferenceCount() const
    {
        return m_ref_count;
    }
private:
    int m_ref_count;
};

template<typename T>
class Shared_Ptr 
{
public:
    Shared_Ptr():
        m_pData(nullptr),
        m_pReferenceCountManager(nullptr)
    {}

    ~Shared_Ptr() noexcept
    {
        if (m_pReferenceCountManager) 
        {
            if (m_pReferenceCountManager->decrementReferenceCount() == 0) 
            {
                delete m_pData;
                delete m_pReferenceCountManager;
                m_pData = nullptr;
                m_pReferenceCountManager = nullptr;
            }
        }
    }

    explicit Shared_Ptr(T* ptr):
        m_pData(ptr),
        m_pReferenceCountManager(nullptr)
    {
        m_pReferenceCountManager = new ReferenceCountManager();
        m_pReferenceCountManager->incrementReferenceCount();
    }

    Shared_Ptr(const Shared_Ptr<T>& ob) noexcept :
        m_pData(ob.m_pData),
        m_pReferenceCountManager(ob.m_pReferenceCountManager)
    {
        m_pReferenceCountManager->incrementReferenceCount();
    }

    Shared_Ptr<T>& operator = (const Shared_Ptr<T>& ob) noexcept
    {
        Shared_Ptr(ob).swap(*this);
        return *this;
    }

    Shared_Ptr(Shared_Ptr<T>&& ob) noexcept :
        m_pData(ob.m_pData),
        m_pReferenceCountManager(ob.m_pReferenceCountManager)
    {
        ob.m_pData = nullptr;
        ob.m_pReferenceCountManager = nullptr;
    }

    Shared_Ptr<T>& operator = (Shared_Ptr<T> &&ob) noexcept
    {
        Shared_Ptr(std::move(ob)).swap(*this);
        return *this;
    }

    T& operator* () const
    {
        return *m_pData;
    }

    T* operator-> () const noexcept
    {
        return m_pData;
    }

    T* get() const noexcept
    {
        return m_pData;
    }

    int use_count() const noexcept
    {
        if (m_pReferenceCountManager) 
        {
            return m_pReferenceCountManager->getReferenceCount();
        }
        return 0;
    }

    bool unique() const noexcept
    {   
        return (this->use_count() == 1);
    }

    explicit operator bool() const noexcept
    {   
        return (m_pData != nullptr);
    }

    void reset() noexcept
    {   
        Shared_Ptr().swap(*this);
    }

    void reset(T *ptr)
    {   
        Shared_Ptr(ptr).swap(*this);
    }

    void swap(Shared_Ptr<T>& ob) noexcept 
    {
        using std::swap;
        swap(m_pData, ob.m_pData);
        swap(m_pReferenceCountManager, ob.m_pReferenceCountManager);
    }


private:
    T* m_pData;
    ReferenceCountManager * m_pReferenceCountManager;
};

template<typename T1, typename T2>
bool operator == (const Shared_Ptr<T1>& ob1, const Shared_Ptr<T2>& ob2) noexcept
{
    return ob1.get() == ob2.get();
}

template<typename T1, typename T2>
bool operator != (const Shared_Ptr<T1>& ob1, const Shared_Ptr<T2>& ob2) noexcept
{
    return !(ob1 == ob2);
}

}
