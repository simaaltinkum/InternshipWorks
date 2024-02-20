using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Anasayfa
{
    public partial class Form4 : Form
    {
        public Form4()
        {
            InitializeComponent();
        }

        private void ziyaretBindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.ziyaretBindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.databaseDataSet);

        }

        private void Form4_Load(object sender, EventArgs e)
        {
            // TODO: Bu kod satırı 'databaseDataSet.uye' tablosuna veri yükler. Bunu gerektiği şekilde taşıyabilir, veya kaldırabilirsiniz.
            this.uyeTableAdapter.Fill(this.databaseDataSet.uye);
            // TODO: Bu kod satırı 'databaseDataSet.ziyaret' tablosuna veri yükler. Bunu gerektiği şekilde taşıyabilir, veya kaldırabilirsiniz.
            this.ziyaretTableAdapter.Fill(this.databaseDataSet.ziyaret);
            adCheckedListBox.DataSource = databaseDataSet.uye;
            adCheckedListBox.DisplayMember = "Ad";

            
        }

        private void adresLabel_Click(object sender, EventArgs e)
        {

        }

        private void e_PostaLabel_Click(object sender, EventArgs e)
        {

        }

        private void medeni_DurumComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void adCheckedListBox_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void adComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void uyeBindingSource_CurrentChanged(object sender, EventArgs e)
        {

        }

        private void adCheckedListBox_SelectedIndexChanged_1(object sender, EventArgs e)
        {
            if (adCheckedListBox.CheckedItems.Count != 0)
            {
                // If so, loop through all checked items and print results.  
                string s = "";
                for (int x = 0; x <= adCheckedListBox.CheckedItems.Count - 1; x++)
                {
                    s = s + "Checked Item " + (x + 1).ToString() + " = " + adCheckedListBox.CheckedItems[x].ToString() + "\n";
                }
                MessageBox.Show(s);
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            StringBuilder selectedAds = new StringBuilder();

            foreach (var item in adCheckedListBox.CheckedItems)
            {
                DataRowView row = item as DataRowView;
                if (row != null)
                {
                    string ad = row["Ad"].ToString();
                    selectedAds.AppendLine(ad); // Her bir adı yeni bir satıra eklemek için
                }
            }

            textBox1.Text = selectedAds.ToString(); // TextBox'a seçili adları eklemek
        }
    }
}
