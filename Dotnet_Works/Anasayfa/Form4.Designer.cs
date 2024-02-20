namespace Anasayfa
{
    partial class Form4
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.Windows.Forms.Label adLabel;
            System.Windows.Forms.Label soyadLabel;
            System.Windows.Forms.Label adresLabel;
            System.Windows.Forms.Label telefonLabel;
            System.Windows.Forms.Label e_PostaLabel;
            System.Windows.Forms.Label medeni_DurumLabel;
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form4));
            System.Windows.Forms.Label adLabel1;
            this.databaseDataSet = new Anasayfa.databaseDataSet();
            this.ziyaretBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.ziyaretTableAdapter = new Anasayfa.databaseDataSetTableAdapters.ziyaretTableAdapter();
            this.tableAdapterManager = new Anasayfa.databaseDataSetTableAdapters.TableAdapterManager();
            this.ziyaretBindingNavigator = new System.Windows.Forms.BindingNavigator(this.components);
            this.bindingNavigatorAddNewItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorCountItem = new System.Windows.Forms.ToolStripLabel();
            this.bindingNavigatorDeleteItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMoveFirstItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMovePreviousItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorSeparator = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorPositionItem = new System.Windows.Forms.ToolStripTextBox();
            this.bindingNavigatorSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorMoveNextItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMoveLastItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.ziyaretBindingNavigatorSaveItem = new System.Windows.Forms.ToolStripButton();
            this.adTextBox = new System.Windows.Forms.TextBox();
            this.soyadTextBox = new System.Windows.Forms.TextBox();
            this.adresTextBox = new System.Windows.Forms.TextBox();
            this.telefonTextBox = new System.Windows.Forms.TextBox();
            this.e_PostaTextBox = new System.Windows.Forms.TextBox();
            this.ziyaretDataGridView = new System.Windows.Forms.DataGridView();
            this.dataGridViewTextBoxColumn1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn2 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn3 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn4 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn5 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn6 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn7 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.medeni_DurumComboBox = new System.Windows.Forms.ComboBox();
            this.uyeBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.uyeTableAdapter = new Anasayfa.databaseDataSetTableAdapters.uyeTableAdapter();
            this.adCheckedListBox = new System.Windows.Forms.CheckedListBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            adLabel = new System.Windows.Forms.Label();
            soyadLabel = new System.Windows.Forms.Label();
            adresLabel = new System.Windows.Forms.Label();
            telefonLabel = new System.Windows.Forms.Label();
            e_PostaLabel = new System.Windows.Forms.Label();
            medeni_DurumLabel = new System.Windows.Forms.Label();
            adLabel1 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.databaseDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.ziyaretBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.ziyaretBindingNavigator)).BeginInit();
            this.ziyaretBindingNavigator.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.ziyaretDataGridView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.uyeBindingSource)).BeginInit();
            this.SuspendLayout();
            // 
            // adLabel
            // 
            adLabel.AutoSize = true;
            adLabel.Location = new System.Drawing.Point(13, 68);
            adLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            adLabel.Name = "adLabel";
            adLabel.Size = new System.Drawing.Size(43, 25);
            adLabel.TabIndex = 1;
            adLabel.Text = "Ad:";
            // 
            // soyadLabel
            // 
            soyadLabel.AutoSize = true;
            soyadLabel.Location = new System.Drawing.Point(13, 136);
            soyadLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            soyadLabel.Name = "soyadLabel";
            soyadLabel.Size = new System.Drawing.Size(75, 25);
            soyadLabel.TabIndex = 3;
            soyadLabel.Text = "Soyad:";
            // 
            // adresLabel
            // 
            adresLabel.AutoSize = true;
            adresLabel.Location = new System.Drawing.Point(13, 198);
            adresLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            adresLabel.Name = "adresLabel";
            adresLabel.Size = new System.Drawing.Size(70, 25);
            adresLabel.TabIndex = 5;
            adresLabel.Text = "Adres:";
            adresLabel.Click += new System.EventHandler(this.adresLabel_Click);
            // 
            // telefonLabel
            // 
            telefonLabel.AutoSize = true;
            telefonLabel.Location = new System.Drawing.Point(13, 253);
            telefonLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            telefonLabel.Name = "telefonLabel";
            telefonLabel.Size = new System.Drawing.Size(84, 25);
            telefonLabel.TabIndex = 7;
            telefonLabel.Text = "Telefon:";
            // 
            // e_PostaLabel
            // 
            e_PostaLabel.AutoSize = true;
            e_PostaLabel.Location = new System.Drawing.Point(13, 307);
            e_PostaLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            e_PostaLabel.Name = "e_PostaLabel";
            e_PostaLabel.Size = new System.Drawing.Size(86, 25);
            e_PostaLabel.TabIndex = 9;
            e_PostaLabel.Text = "E Posta:";
            e_PostaLabel.Click += new System.EventHandler(this.e_PostaLabel_Click);
            // 
            // medeni_DurumLabel
            // 
            medeni_DurumLabel.AutoSize = true;
            medeni_DurumLabel.Location = new System.Drawing.Point(13, 365);
            medeni_DurumLabel.Name = "medeni_DurumLabel";
            medeni_DurumLabel.Size = new System.Drawing.Size(146, 25);
            medeni_DurumLabel.TabIndex = 13;
            medeni_DurumLabel.Text = "Medeni Durum:";
            // 
            // databaseDataSet
            // 
            this.databaseDataSet.DataSetName = "databaseDataSet";
            this.databaseDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // ziyaretBindingSource
            // 
            this.ziyaretBindingSource.DataMember = "ziyaret";
            this.ziyaretBindingSource.DataSource = this.databaseDataSet;
            // 
            // ziyaretTableAdapter
            // 
            this.ziyaretTableAdapter.ClearBeforeFill = true;
            // 
            // tableAdapterManager
            // 
            this.tableAdapterManager.BackupDataSetBeforeUpdate = false;
            this.tableAdapterManager.UpdateOrder = Anasayfa.databaseDataSetTableAdapters.TableAdapterManager.UpdateOrderOption.InsertUpdateDelete;
            this.tableAdapterManager.uyeTableAdapter = null;
            this.tableAdapterManager.ziyaretTableAdapter = this.ziyaretTableAdapter;
            // 
            // ziyaretBindingNavigator
            // 
            this.ziyaretBindingNavigator.AddNewItem = this.bindingNavigatorAddNewItem;
            this.ziyaretBindingNavigator.BindingSource = this.ziyaretBindingSource;
            this.ziyaretBindingNavigator.CountItem = this.bindingNavigatorCountItem;
            this.ziyaretBindingNavigator.DataBindings.Add(new System.Windows.Forms.Binding("Tag", this.uyeBindingSource, "Ad", true));
            this.ziyaretBindingNavigator.DeleteItem = this.bindingNavigatorDeleteItem;
            this.ziyaretBindingNavigator.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.ziyaretBindingNavigator.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.bindingNavigatorMoveFirstItem,
            this.bindingNavigatorMovePreviousItem,
            this.bindingNavigatorSeparator,
            this.bindingNavigatorPositionItem,
            this.bindingNavigatorCountItem,
            this.bindingNavigatorSeparator1,
            this.bindingNavigatorMoveNextItem,
            this.bindingNavigatorMoveLastItem,
            this.bindingNavigatorSeparator2,
            this.bindingNavigatorAddNewItem,
            this.bindingNavigatorDeleteItem,
            this.ziyaretBindingNavigatorSaveItem});
            this.ziyaretBindingNavigator.Location = new System.Drawing.Point(0, 0);
            this.ziyaretBindingNavigator.MoveFirstItem = this.bindingNavigatorMoveFirstItem;
            this.ziyaretBindingNavigator.MoveLastItem = this.bindingNavigatorMoveLastItem;
            this.ziyaretBindingNavigator.MoveNextItem = this.bindingNavigatorMoveNextItem;
            this.ziyaretBindingNavigator.MovePreviousItem = this.bindingNavigatorMovePreviousItem;
            this.ziyaretBindingNavigator.Name = "ziyaretBindingNavigator";
            this.ziyaretBindingNavigator.Padding = new System.Windows.Forms.Padding(0, 0, 2, 0);
            this.ziyaretBindingNavigator.PositionItem = this.bindingNavigatorPositionItem;
            this.ziyaretBindingNavigator.Size = new System.Drawing.Size(1200, 27);
            this.ziyaretBindingNavigator.TabIndex = 0;
            this.ziyaretBindingNavigator.Text = "bindingNavigator1";
            // 
            // bindingNavigatorAddNewItem
            // 
            this.bindingNavigatorAddNewItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorAddNewItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorAddNewItem.Image")));
            this.bindingNavigatorAddNewItem.Name = "bindingNavigatorAddNewItem";
            this.bindingNavigatorAddNewItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorAddNewItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorAddNewItem.Text = "Yeni ekle";
            // 
            // bindingNavigatorCountItem
            // 
            this.bindingNavigatorCountItem.Name = "bindingNavigatorCountItem";
            this.bindingNavigatorCountItem.Size = new System.Drawing.Size(37, 24);
            this.bindingNavigatorCountItem.Text = "/ {0}";
            this.bindingNavigatorCountItem.ToolTipText = "Toplam öğe sayısı";
            // 
            // bindingNavigatorDeleteItem
            // 
            this.bindingNavigatorDeleteItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorDeleteItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorDeleteItem.Image")));
            this.bindingNavigatorDeleteItem.Name = "bindingNavigatorDeleteItem";
            this.bindingNavigatorDeleteItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorDeleteItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorDeleteItem.Text = "Sil";
            // 
            // bindingNavigatorMoveFirstItem
            // 
            this.bindingNavigatorMoveFirstItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveFirstItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveFirstItem.Image")));
            this.bindingNavigatorMoveFirstItem.Name = "bindingNavigatorMoveFirstItem";
            this.bindingNavigatorMoveFirstItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveFirstItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorMoveFirstItem.Text = "Başa taşı";
            // 
            // bindingNavigatorMovePreviousItem
            // 
            this.bindingNavigatorMovePreviousItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMovePreviousItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMovePreviousItem.Image")));
            this.bindingNavigatorMovePreviousItem.Name = "bindingNavigatorMovePreviousItem";
            this.bindingNavigatorMovePreviousItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMovePreviousItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorMovePreviousItem.Text = "Öne taşı";
            // 
            // bindingNavigatorSeparator
            // 
            this.bindingNavigatorSeparator.Name = "bindingNavigatorSeparator";
            this.bindingNavigatorSeparator.Size = new System.Drawing.Size(6, 27);
            // 
            // bindingNavigatorPositionItem
            // 
            this.bindingNavigatorPositionItem.AccessibleName = "Konum";
            this.bindingNavigatorPositionItem.AutoSize = false;
            this.bindingNavigatorPositionItem.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.bindingNavigatorPositionItem.Name = "bindingNavigatorPositionItem";
            this.bindingNavigatorPositionItem.Size = new System.Drawing.Size(50, 27);
            this.bindingNavigatorPositionItem.Text = "0";
            this.bindingNavigatorPositionItem.ToolTipText = "Geçerli konum";
            // 
            // bindingNavigatorSeparator1
            // 
            this.bindingNavigatorSeparator1.Name = "bindingNavigatorSeparator1";
            this.bindingNavigatorSeparator1.Size = new System.Drawing.Size(6, 27);
            // 
            // bindingNavigatorMoveNextItem
            // 
            this.bindingNavigatorMoveNextItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveNextItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveNextItem.Image")));
            this.bindingNavigatorMoveNextItem.Name = "bindingNavigatorMoveNextItem";
            this.bindingNavigatorMoveNextItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveNextItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorMoveNextItem.Text = "Arkaya taşı";
            // 
            // bindingNavigatorMoveLastItem
            // 
            this.bindingNavigatorMoveLastItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveLastItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveLastItem.Image")));
            this.bindingNavigatorMoveLastItem.Name = "bindingNavigatorMoveLastItem";
            this.bindingNavigatorMoveLastItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveLastItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorMoveLastItem.Text = "Sona taşı";
            // 
            // bindingNavigatorSeparator2
            // 
            this.bindingNavigatorSeparator2.Name = "bindingNavigatorSeparator2";
            this.bindingNavigatorSeparator2.Size = new System.Drawing.Size(6, 27);
            // 
            // ziyaretBindingNavigatorSaveItem
            // 
            this.ziyaretBindingNavigatorSaveItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.ziyaretBindingNavigatorSaveItem.Image = ((System.Drawing.Image)(resources.GetObject("ziyaretBindingNavigatorSaveItem.Image")));
            this.ziyaretBindingNavigatorSaveItem.Name = "ziyaretBindingNavigatorSaveItem";
            this.ziyaretBindingNavigatorSaveItem.Size = new System.Drawing.Size(29, 24);
            this.ziyaretBindingNavigatorSaveItem.Text = "Veriyi Sakla";
            this.ziyaretBindingNavigatorSaveItem.Click += new System.EventHandler(this.ziyaretBindingNavigatorSaveItem_Click);
            // 
            // adTextBox
            // 
            this.adTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.ziyaretBindingSource, "Ad", true));
            this.adTextBox.Location = new System.Drawing.Point(172, 68);
            this.adTextBox.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.adTextBox.Name = "adTextBox";
            this.adTextBox.Size = new System.Drawing.Size(148, 30);
            this.adTextBox.TabIndex = 2;
            // 
            // soyadTextBox
            // 
            this.soyadTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.ziyaretBindingSource, "Soyad", true));
            this.soyadTextBox.Location = new System.Drawing.Point(172, 136);
            this.soyadTextBox.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.soyadTextBox.Name = "soyadTextBox";
            this.soyadTextBox.Size = new System.Drawing.Size(148, 30);
            this.soyadTextBox.TabIndex = 4;
            // 
            // adresTextBox
            // 
            this.adresTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.ziyaretBindingSource, "Adres", true));
            this.adresTextBox.Location = new System.Drawing.Point(172, 198);
            this.adresTextBox.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.adresTextBox.Name = "adresTextBox";
            this.adresTextBox.Size = new System.Drawing.Size(148, 30);
            this.adresTextBox.TabIndex = 6;
            // 
            // telefonTextBox
            // 
            this.telefonTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.ziyaretBindingSource, "Telefon", true));
            this.telefonTextBox.Location = new System.Drawing.Point(172, 253);
            this.telefonTextBox.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.telefonTextBox.Name = "telefonTextBox";
            this.telefonTextBox.Size = new System.Drawing.Size(148, 30);
            this.telefonTextBox.TabIndex = 8;
            // 
            // e_PostaTextBox
            // 
            this.e_PostaTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.ziyaretBindingSource, "E Posta", true));
            this.e_PostaTextBox.Location = new System.Drawing.Point(172, 307);
            this.e_PostaTextBox.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.e_PostaTextBox.Name = "e_PostaTextBox";
            this.e_PostaTextBox.Size = new System.Drawing.Size(148, 30);
            this.e_PostaTextBox.TabIndex = 10;
            // 
            // ziyaretDataGridView
            // 
            this.ziyaretDataGridView.AutoGenerateColumns = false;
            this.ziyaretDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.ziyaretDataGridView.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.dataGridViewTextBoxColumn1,
            this.dataGridViewTextBoxColumn2,
            this.dataGridViewTextBoxColumn3,
            this.dataGridViewTextBoxColumn4,
            this.dataGridViewTextBoxColumn5,
            this.dataGridViewTextBoxColumn6,
            this.dataGridViewTextBoxColumn7});
            this.ziyaretDataGridView.DataSource = this.ziyaretBindingSource;
            this.ziyaretDataGridView.Location = new System.Drawing.Point(28, 499);
            this.ziyaretDataGridView.Name = "ziyaretDataGridView";
            this.ziyaretDataGridView.RowHeadersWidth = 51;
            this.ziyaretDataGridView.RowTemplate.Height = 24;
            this.ziyaretDataGridView.Size = new System.Drawing.Size(930, 220);
            this.ziyaretDataGridView.TabIndex = 13;
            // 
            // dataGridViewTextBoxColumn1
            // 
            this.dataGridViewTextBoxColumn1.DataPropertyName = "Id";
            this.dataGridViewTextBoxColumn1.HeaderText = "Id";
            this.dataGridViewTextBoxColumn1.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn1.Name = "dataGridViewTextBoxColumn1";
            this.dataGridViewTextBoxColumn1.Width = 125;
            // 
            // dataGridViewTextBoxColumn2
            // 
            this.dataGridViewTextBoxColumn2.DataPropertyName = "Ad";
            this.dataGridViewTextBoxColumn2.HeaderText = "Ad";
            this.dataGridViewTextBoxColumn2.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn2.Name = "dataGridViewTextBoxColumn2";
            this.dataGridViewTextBoxColumn2.Width = 125;
            // 
            // dataGridViewTextBoxColumn3
            // 
            this.dataGridViewTextBoxColumn3.DataPropertyName = "Soyad";
            this.dataGridViewTextBoxColumn3.HeaderText = "Soyad";
            this.dataGridViewTextBoxColumn3.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn3.Name = "dataGridViewTextBoxColumn3";
            this.dataGridViewTextBoxColumn3.Width = 125;
            // 
            // dataGridViewTextBoxColumn4
            // 
            this.dataGridViewTextBoxColumn4.DataPropertyName = "Adres";
            this.dataGridViewTextBoxColumn4.HeaderText = "Adres";
            this.dataGridViewTextBoxColumn4.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn4.Name = "dataGridViewTextBoxColumn4";
            this.dataGridViewTextBoxColumn4.Width = 125;
            // 
            // dataGridViewTextBoxColumn5
            // 
            this.dataGridViewTextBoxColumn5.DataPropertyName = "Telefon";
            this.dataGridViewTextBoxColumn5.HeaderText = "Telefon";
            this.dataGridViewTextBoxColumn5.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn5.Name = "dataGridViewTextBoxColumn5";
            this.dataGridViewTextBoxColumn5.Width = 125;
            // 
            // dataGridViewTextBoxColumn6
            // 
            this.dataGridViewTextBoxColumn6.DataPropertyName = "E Posta";
            this.dataGridViewTextBoxColumn6.HeaderText = "E Posta";
            this.dataGridViewTextBoxColumn6.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn6.Name = "dataGridViewTextBoxColumn6";
            this.dataGridViewTextBoxColumn6.Width = 125;
            // 
            // dataGridViewTextBoxColumn7
            // 
            this.dataGridViewTextBoxColumn7.DataPropertyName = "Medeni Durum";
            this.dataGridViewTextBoxColumn7.HeaderText = "Medeni Durum";
            this.dataGridViewTextBoxColumn7.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn7.Name = "dataGridViewTextBoxColumn7";
            this.dataGridViewTextBoxColumn7.Width = 125;
            // 
            // medeni_DurumComboBox
            // 
            this.medeni_DurumComboBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.ziyaretBindingSource, "Medeni Durum", true));
            this.medeni_DurumComboBox.FormattingEnabled = true;
            this.medeni_DurumComboBox.Items.AddRange(new object[] {
            "Bekar",
            "Evli"});
            this.medeni_DurumComboBox.Location = new System.Drawing.Point(172, 365);
            this.medeni_DurumComboBox.Name = "medeni_DurumComboBox";
            this.medeni_DurumComboBox.Size = new System.Drawing.Size(148, 33);
            this.medeni_DurumComboBox.TabIndex = 14;
            this.medeni_DurumComboBox.SelectedIndexChanged += new System.EventHandler(this.medeni_DurumComboBox_SelectedIndexChanged);
            // 
            // uyeBindingSource
            // 
            this.uyeBindingSource.DataMember = "uye";
            this.uyeBindingSource.DataSource = this.databaseDataSet;
            this.uyeBindingSource.CurrentChanged += new System.EventHandler(this.uyeBindingSource_CurrentChanged);
            // 
            // uyeTableAdapter
            // 
            this.uyeTableAdapter.ClearBeforeFill = true;
            // 
            // adLabel1
            // 
            adLabel1.AutoSize = true;
            adLabel1.DataBindings.Add(new System.Windows.Forms.Binding("Tag", this.uyeBindingSource, "Ad", true));
            adLabel1.Location = new System.Drawing.Point(396, 68);
            adLabel1.Name = "adLabel1";
            adLabel1.Size = new System.Drawing.Size(43, 25);
            adLabel1.TabIndex = 17;
            adLabel1.Text = "Ad:";
            // 
            // adCheckedListBox
            // 
            this.adCheckedListBox.DataBindings.Add(new System.Windows.Forms.Binding("SelectedValue", this.uyeBindingSource, "Ad", true));
            this.adCheckedListBox.DataBindings.Add(new System.Windows.Forms.Binding("Tag", this.uyeBindingSource, "Ad", true));
            this.adCheckedListBox.FormattingEnabled = true;
            this.adCheckedListBox.Location = new System.Drawing.Point(502, 68);
            this.adCheckedListBox.Name = "adCheckedListBox";
            this.adCheckedListBox.Size = new System.Drawing.Size(250, 79);
            this.adCheckedListBox.TabIndex = 18;
            this.adCheckedListBox.SelectedIndexChanged += new System.EventHandler(this.adCheckedListBox_SelectedIndexChanged_1);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(22, 432);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(297, 30);
            this.textBox1.TabIndex = 19;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // Form4
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1200, 739);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(adLabel1);
            this.Controls.Add(this.adCheckedListBox);
            this.Controls.Add(medeni_DurumLabel);
            this.Controls.Add(this.medeni_DurumComboBox);
            this.Controls.Add(this.ziyaretDataGridView);
            this.Controls.Add(e_PostaLabel);
            this.Controls.Add(this.e_PostaTextBox);
            this.Controls.Add(telefonLabel);
            this.Controls.Add(this.telefonTextBox);
            this.Controls.Add(adresLabel);
            this.Controls.Add(this.adresTextBox);
            this.Controls.Add(soyadLabel);
            this.Controls.Add(this.soyadTextBox);
            this.Controls.Add(adLabel);
            this.Controls.Add(this.adTextBox);
            this.Controls.Add(this.ziyaretBindingNavigator);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Name = "Form4";
            this.Text = "Form4";
            this.Load += new System.EventHandler(this.Form4_Load);
            ((System.ComponentModel.ISupportInitialize)(this.databaseDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.ziyaretBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.ziyaretBindingNavigator)).EndInit();
            this.ziyaretBindingNavigator.ResumeLayout(false);
            this.ziyaretBindingNavigator.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.ziyaretDataGridView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.uyeBindingSource)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private databaseDataSet databaseDataSet;
        private System.Windows.Forms.BindingSource ziyaretBindingSource;
        private databaseDataSetTableAdapters.ziyaretTableAdapter ziyaretTableAdapter;
        private databaseDataSetTableAdapters.TableAdapterManager tableAdapterManager;
        private System.Windows.Forms.BindingNavigator ziyaretBindingNavigator;
        private System.Windows.Forms.ToolStripButton bindingNavigatorAddNewItem;
        private System.Windows.Forms.ToolStripLabel bindingNavigatorCountItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorDeleteItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveFirstItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMovePreviousItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator;
        private System.Windows.Forms.ToolStripTextBox bindingNavigatorPositionItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator1;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveNextItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveLastItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator2;
        private System.Windows.Forms.ToolStripButton ziyaretBindingNavigatorSaveItem;
        private System.Windows.Forms.TextBox adTextBox;
        private System.Windows.Forms.TextBox soyadTextBox;
        private System.Windows.Forms.TextBox adresTextBox;
        private System.Windows.Forms.TextBox telefonTextBox;
        private System.Windows.Forms.TextBox e_PostaTextBox;
        private System.Windows.Forms.DataGridView ziyaretDataGridView;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn1;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn2;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn3;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn4;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn5;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn6;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn7;
        private System.Windows.Forms.ComboBox medeni_DurumComboBox;
        private System.Windows.Forms.BindingSource uyeBindingSource;
        private databaseDataSetTableAdapters.uyeTableAdapter uyeTableAdapter;
        private System.Windows.Forms.CheckedListBox adCheckedListBox;
        private System.Windows.Forms.TextBox textBox1;
    }
}